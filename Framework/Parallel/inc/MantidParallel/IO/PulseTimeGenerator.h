#ifndef MANTID_PARALLEL_PULSETIMEGENERATOR_H_
#define MANTID_PARALLEL_PULSETIMEGENERATOR_H_

#include "MantidParallel/DllConfig.h"
#include "MantidTypes/Core/DateAndTime.h"

namespace Mantid {
namespace Parallel {
namespace IO {

/** Generator for pulse times based in input from an NXevent_data entry from a
  Nexus file. Used to generate a sequence of pulse times for a series of events
  by doing a lookup of the event in the event_index field and returning the
  corresponding pulse time obtained from event_time_zero combined with the
  optional offset parameter.

  @author Simon Heybrock
  @date 2017

  Copyright &copy; 2017 ISIS Rutherford Appleton Laboratory, NScD Oak Ridge
  National Laboratory & European Spallation Source

  This file is part of Mantid.

  Mantid is free software; you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation; either version 3 of the License, or
  (at your option) any later version.

  Mantid is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program.  If not, see <http://www.gnu.org/licenses/>.

  File change history is stored at: <https://github.com/mantidproject/mantid>
  Code Documentation is available at: <http://doxygen.mantidproject.org>
*/
namespace detail {
template <class TimeZeroType>
Types::Core::DateAndTime getPulseTime(const Types::Core::DateAndTime &offset,
                                      const TimeZeroType &eventTimeZero) {
  return offset + eventTimeZero;
}

template <>
inline Types::Core::DateAndTime
getPulseTime<uint64_t>(const Types::Core::DateAndTime &offset,
                       const uint64_t &eventTimeZero) {
  return offset + static_cast<int64_t>(eventTimeZero);
}

template <>
inline Types::Core::DateAndTime
getPulseTime<int32_t>(const Types::Core::DateAndTime &offset,
                      const int32_t &eventTimeZero) {
  return offset + static_cast<int64_t>(eventTimeZero);
}

template <>
inline Types::Core::DateAndTime
getPulseTime<uint32_t>(const Types::Core::DateAndTime &offset,
                       const uint32_t &eventTimeZero) {
  return offset + static_cast<int64_t>(eventTimeZero);
}
}

template <class IndexType, class TimeZeroType> class PulseTimeGenerator {
public:
  PulseTimeGenerator() = default;

  /// Constructor based on entries in NXevent_data.
  PulseTimeGenerator(std::vector<IndexType> event_index,
                     std::vector<TimeZeroType> event_time_zero,
                     const int64_t event_time_zero_offset)
      : m_index(std::move(event_index)), m_timeZero(std::move(event_time_zero)),
        m_timeZeroOffset(event_time_zero_offset) {}

  /// Seek to given event index.
  void seek(const size_t event) {
    if (m_index.size() == 0)
      throw std::runtime_error("Empty event index in PulseTimeGenerator");
    if (static_cast<IndexType>(event) < m_event)
      m_pulse = 0;
    m_event = static_cast<IndexType>(event);
    for (; m_pulse < m_index.size() - 1; ++m_pulse)
      if (m_event < m_index[m_pulse + 1])
        break;
    m_pulseTime = detail::getPulseTime(m_timeZeroOffset, m_timeZero[m_pulse]);
  }

  /// Return pulse time for next event, and advance.
  Types::Core::DateAndTime next() {
    while (m_pulse < m_index.size() - 1 && m_event == m_index[m_pulse + 1]) {
      ++m_pulse;
      m_pulseTime = detail::getPulseTime(m_timeZeroOffset, m_timeZero[m_pulse]);
    }
    ++m_event;
    return m_pulseTime;
  }

private:
  IndexType m_event{0};
  size_t m_pulse{0};
  Types::Core::DateAndTime m_pulseTime;
  std::vector<IndexType> m_index;
  std::vector<TimeZeroType> m_timeZero;
  Types::Core::DateAndTime m_timeZeroOffset;
};

} // namespace IO
} // namespace Parallel
} // namespace Mantid

#endif /* MANTID_PARALLEL_PULSETIMEGENERATOR_H_ */
