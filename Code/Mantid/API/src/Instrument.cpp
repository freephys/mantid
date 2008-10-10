#include "MantidAPI/Instrument.h"
#include "MantidGeometry/V3D.h"
#include "MantidKernel/Exception.h"
#include "MantidGeometry/DetectorGroup.h"
#include <algorithm>

namespace Mantid
{
namespace API
{

Kernel::Logger& Instrument::g_log = Kernel::Logger::get("Instrument");

/// Default constructor
Instrument::Instrument() : Geometry::CompAssembly(),
                           _detectorCache(),_sourceCache(0),_sampleCache(0)
{}

/// Constructor with name
Instrument::Instrument(const std::string& name) : Geometry::CompAssembly(name),
                           _detectorCache(),_sourceCache(0),_sampleCache(0)
{}

/**	Gets a pointer to the source
* @returns a pointer to the source
*/
Geometry::ObjComponent* Instrument::getSource() const
{
  if ( !_sourceCache )
    g_log.warning("In Instrument::getSource(). No source has been set.");
  return _sourceCache;
}

/**	Gets a pointer to the Sample Position
* @returns a pointer to the Sample Position
*/
Geometry::ObjComponent* Instrument::getSample() const
{
  if ( !_sampleCache )
    g_log.warning("In Instrument::getSamplePos(). No SamplePos has been set.");
  return _sampleCache;
}

/**	Gets a pointer to the detector from its ID
 *  Note that for getting the detector associated with a spectrum, the SpectraDetectorMap::getDetector
 *  method should be used rather than this one because it takes account of the possibility of more
 *  than one detector contibuting to a single spectrum
 *  @param   detector_id The requested detector ID
 *  @returns A pointer to the detector object
 *  @throw   NotFoundError If no detector is found for the detector ID given
 */
Geometry::IDetector* Instrument::getDetector(const int &detector_id) const
{
  std::map<int, Geometry::IDetector*>::const_iterator it;

  it = _detectorCache.find(detector_id);

  if ( it == _detectorCache.end() )
  {
    g_log.debug() << "Detector with ID " << detector_id << " not found." << std::endl;
    throw Kernel::Exception::NotFoundError("Instrument: Detector is not found.","");
  }

  return it->second;
}

/** Returns the 2Theta scattering angle for a detector
 *  @param det A pointer to the detector object (N.B. might be a DetectorGroup)
 *  @return The scattering angle (0 < theta < pi)
 */
const double Instrument::detectorTwoTheta(const Geometry::IDetector* const det) const
{
  const Geometry::V3D samplePos = this->getSample()->getPos();
  const Geometry::V3D beamLine = samplePos - this->getSource()->getPos();
  const Geometry::V3D sampleDetVec = det->getPos() - samplePos;
  return sampleDetVec.angle(beamLine);
}

/**	Gets a pointer to the requested child component
* @param name the name of the object requested (case insensitive)
* @returns a pointer to the component
*/
Geometry::Component* Instrument::getChild(const std::string& name) const
{
  Geometry::Component *retVal = 0;
  std::string searchName = name;
  std::transform(searchName.begin(), searchName.end(), searchName.begin(), toupper);

  int noOfChildren = this->nelements();
  for (int i = 0; i < noOfChildren; i++)
  {
    Geometry::Component *loopPtr = (*this)[i];
    std::string loopName = loopPtr->getName();
    std::transform(loopName.begin(), loopName.end(), loopName.begin(), toupper);
    if (loopName == searchName)
    {
      retVal = loopPtr;
    }
  }

  if (!retVal)
  {
    throw Kernel::Exception::NotFoundError("Instrument: Child "+ name + " is not found.",name);
  }

  return retVal;
}

/** Mark a Component which has already been added to the Instrument (as a child component)
* to be 'the' samplePos Component. For now it is assumed that we have
* at most one of these.
*
* @param comp Component to be marked (stored for later retrievel) as a "SamplePos" Component
*/
void Instrument::markAsSamplePos(Geometry::ObjComponent* comp)
{
  if ( !_sampleCache )
    _sampleCache = comp;
  else
    g_log.warning("Have already added samplePos component to the _sampleCache.");
}

/** Mark a Component which has already been added to the Instrument (as a child component)
* to be 'the' source Component. For now it is assumed that we have
* at most one of these.
*
* @param comp Component to be marked (stored for later retrievel) as a "source" Component
*/
void Instrument::markAsSource(Geometry::ObjComponent* comp)
{
  if ( !_sourceCache )
    _sourceCache = comp;
  else
    g_log.warning("Have already added source component to the _sourceCache.");
}

/** Mark a Component which has already been added to the Instrument (as a child component)
* to be a Detector by adding it to a detector cache.
*
* @param det Component to be marked (stored for later retrievel) as a detector Component
*
* @throw Exception::ExistsError if cannot add detector to cache
*/
void Instrument::markAsDetector(Geometry::IDetector* det)
{
  if ( !_detectorCache.insert( std::map<int, Geometry::IDetector*>::value_type(det->getID(), det) ).second )
  {
    std::stringstream convert;
    convert << det->getID();
    g_log.error() << "Not successful in adding Detector " << convert << " to _detectorCache." << std::endl;
    throw Kernel::Exception::ExistsError("Not successful in adding Detector to _detectorCache.", convert.str());
  }
}

/** Mark a Component which has already been added to the Instrument class
* as a monitor and add it to the detector cache.
*
* @param det Component to be marked (stored for later retrievel) as a detector Component
*
* @throw Exception::ExistsError if cannot add detector to cache
*/
void Instrument::markAsMonitor(Geometry::IDetector* det)
{
  // attempt to add monitor to instrument detector cache
  markAsDetector(det);

  // mark detector as a monitor
  Geometry::Detector *d = dynamic_cast<Geometry::Detector*>(det);
  if (d)
  {
    d->markAsMonitor();
  }
  else
  {
    throw std::invalid_argument("The IDetector pointer does not point to a Detector object");
  }
}


} // namespace API
} // Namespace Mantid
