#ifndef MANTID_PYTHONINTERFACE_TYPEDPROPERTYVALUEHANDLER_H_
#define MANTID_PYTHONINTERFACE_TYPEDPROPERTYVALUEHANDLER_H_
/**
    Copyright &copy; 2011 ISIS Rutherford Appleton Laboratory, NScD Oak Ridge
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
#include "MantidPythonInterface/api/ExtractWorkspace.h"
#include "MantidPythonInterface/kernel/Registry/PropertyValueHandler.h"
#include "MantidPythonInterface/kernel/IsNone.h" // includes object.hpp

#include "MantidAPI/Workspace.h"
#include "MantidKernel/PropertyWithValue.h"
#include "MantidKernel/IPropertyManager.h"

#include <boost/python/converter/arg_from_python.hpp>
#include <boost/python/call_method.hpp>
#include <boost/python/extract.hpp>
#include <boost/weak_ptr.hpp>

#include <string>

namespace Mantid {
namespace PythonInterface {
namespace Registry {
/**
 * This class provides a templated class object that is able to take a
 * python object and perform operations with a given C type.
 */
template <typename ValueType, typename Enable = void>
struct DLLExport TypedPropertyValueHandler : public PropertyValueHandler {
  /// Type required by TypeRegistry framework
  typedef ValueType HeldType;

  /**
   * Set function to handle Python -> C++ calls and get the correct type
   * @param alg :: A pointer to an IPropertyManager
   * @param name :: The name of the property
   * @param value :: A boost python object that stores the value
   */
  void set(Kernel::IPropertyManager *alg, const std::string &name,
           const boost::python::object &value) const override {
    alg->setProperty<ValueType>(name, boost::python::extract<ValueType>(value));
  }
  /**
   * Create a PropertyWithValue from the given python object value
   * @param name :: The name of the property
   * @param defaultValue :: The defaultValue of the property. The object
   * attempts to extract
   * a value of type ValueType from the python object
   * @param validator :: A python object pointing to a validator instance, which
   * can be None.
   * @param direction :: The direction of the property
   * @returns A pointer to a newly constructed property instance
   */
  std::unique_ptr<Kernel::Property>
  create(const std::string &name, const boost::python::object &defaultValue,
         const boost::python::object &validator,
         const unsigned int direction) const override {
    using Mantid::Kernel::IValidator;
    using Mantid::Kernel::PropertyWithValue;
    using boost::python::extract;
    const ValueType valueInC = extract<ValueType>(defaultValue)();
    std::unique_ptr<Kernel::Property> valueProp;
    if (isNone(validator)) {
      valueProp = Mantid::Kernel::make_unique<PropertyWithValue<ValueType>>(
          name, valueInC, direction);
    } else {
      const IValidator *propValidator = extract<IValidator *>(validator);
      valueProp = Mantid::Kernel::make_unique<PropertyWithValue<ValueType>>(
          name, valueInC, propValidator->clone(), direction);
    }
    return valueProp;
  }
};

//
// Specialization for shared_ptr types. They need special handling for
// workspaces
//
template <typename T>
struct DLLExport TypedPropertyValueHandler<
    boost::shared_ptr<T>,
    typename std::enable_if<std::is_base_of<API::Workspace, T>::value>::type>
    : public PropertyValueHandler {
  /// Type required by TypeRegistry framework
  typedef boost::shared_ptr<T> HeldType;

  /// Convenience typedef
  typedef T PointeeType;
  /// Convenience typedef
  typedef boost::shared_ptr<T> PropertyValueType;

  /**
   * Set function to handle Python -> C++ calls and get the correct type
   * @param alg :: A pointer to an IPropertyManager
   * @param name :: The name of the property
   * @param value :: A boost python object that stores the value
   */
  void set(Kernel::IPropertyManager *alg, const std::string &name,
           const boost::python::object &value) const override {
    if (value == boost::python::object())
      alg->setProperty<HeldType>(name, boost::shared_ptr<T>(nullptr));
    else
      alg->setProperty<HeldType>(
          name, boost::dynamic_pointer_cast<T>(ExtractWorkspace(value)()));
  }

  /**
   * Create a PropertyWithValue from the given python object value
   * @param name :: The name of the property
   * @param defaultValue :: The defaultValue of the property. The object
   * attempts to extract
   * a value of type ValueType from the python object
   * @param validator :: A python object pointing to a validator instance, which
   * can be None.
   * @param direction :: The direction of the property
   * @returns A pointer to a newly constructed property instance
   */
  std::unique_ptr<Kernel::Property>
  create(const std::string &name, const boost::python::object &defaultValue,
         const boost::python::object &validator,
         const unsigned int direction) const override {
    using Kernel::IValidator;
    using Kernel::Property;
    using Kernel::PropertyWithValue;
    using boost::python::extract;
    const PropertyValueType valueInC =
        extract<PropertyValueType>(defaultValue)();
    std::unique_ptr<Property> valueProp;
    if (isNone(validator)) {
      valueProp =
          Mantid::Kernel::make_unique<PropertyWithValue<PropertyValueType>>(
              name, valueInC, direction);
    } else {
      const IValidator *propValidator = extract<IValidator *>(validator);
      valueProp =
          Mantid::Kernel::make_unique<PropertyWithValue<PropertyValueType>>(
              name, valueInC, propValidator->clone(), direction);
    }
    return valueProp;
  }
};
}
}
}

#endif /* MANTID_PYTHONINTERFACE_TYPEDPROPERTYVALUEHANDLER_H_ */
