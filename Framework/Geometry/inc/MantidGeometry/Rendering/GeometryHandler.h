#ifndef GEOMETRYHANDLER_H
#define GEOMETRYHANDLER_H

#include "MantidGeometry/DllConfig.h"
#include "MantidKernel/Logger.h"
#include "MantidKernel/V3D.h"
#include <boost/shared_ptr.hpp>
#include "MantidGeometry/Rendering/Renderer.h"
#include <vector>
#include <boost/optional.hpp>

namespace Mantid {

namespace Geometry {
class IObjComponent;
class ObjComponent;
class Object;
class GeometryRenderer;

/**
   \class GeometryHandler
   \brief Place holder for geometry triangulation and rendering.
   \author Srikanth Nagella
   \date July 2008
   \version 1.0

   This is an abstract class for handling geometry primitives.

   Copyright &copy; 2008 ISIS Rutherford Appleton Laboratory, NScD Oak Ridge
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
*/
class MANTID_GEOMETRY_DLL GeometryHandler {
private:
  static Kernel::Logger &PLog; ///< The official logger

protected:
  detail::Renderer m_renderer;
  IObjComponent *ObjComp; ///< ObjComponent that uses this geometry handler
  Object *Obj;            ///< Object that uses this geometry handler
  bool boolTriangulated;  ///< state of the geometry triangulation
  bool
      boolIsInitialized; ///< state of the geometry initialization for rendering
public:
  GeometryHandler(IObjComponent *comp);           ///< Constructor
  GeometryHandler(boost::shared_ptr<Object> obj); ///<Constructor
  GeometryHandler(Object *obj);                   ///<Constructor
  GeometryHandler(const GeometryHandler &) = default;
  virtual boost::shared_ptr<GeometryHandler>
  clone() const = 0; ///< Virtual copy constructor
  virtual ~GeometryHandler();
  virtual GeometryHandler *createInstance(IObjComponent *) = 0; ///< Create an
  /// instance of
  /// concrete
  /// geometry
  /// handler for
  /// ObjComponent
  virtual GeometryHandler *
      createInstance(boost::shared_ptr<Object>) = 0; ///< Create an instance of
  /// concrete geometry
  /// handler for Object
  virtual GeometryHandler *createInstance(Object *) = 0; ///< Create an instance
  /// of concrete geometry
  /// handler for Object
  virtual void Triangulate() = 0; ///< Triangulate the Object
  virtual void Render() = 0;      ///< Render Object or ObjComponent
  virtual void
  Initialize() = 0; ///< Prepare/Initialize Object/ObjComponent to be rendered
  /// Returns true if the shape can be triangulated
  virtual bool canTriangulate() { return false; }
  /// get the number of triangles
  virtual size_t numberOfTriangles() { return 0; }
  /// get the number of points or vertices
  virtual size_t numberOfPoints() { return 0; }
  /// Extract the vertices of the triangles
  virtual boost::optional<const std::vector<double> &> getTriangleVertices() {
    return boost::none;
  }
  /// Extract the Faces of the triangles
  virtual boost::optional<const std::vector<int> &> getTriangleFaces() {
    return boost::none;
  }
  /// Sets the geometry cache using the triangulation information provided
  virtual void setGeometryCache(size_t nPts, size_t nFaces,
                                std::vector<double> &&pts,
                                std::vector<int> &&faces) {
    UNUSED_ARG(nPts);
    UNUSED_ARG(nFaces);
    UNUSED_ARG(pts);
    UNUSED_ARG(faces);
  };
  /// return the actual type and points of one of the "standard" objects,
  /// cuboid/cone/cyl/sphere
  virtual void GetObjectGeom(int &mytype, std::vector<Kernel::V3D> &vectors,
                             double &myradius, double &myheight) {
    UNUSED_ARG(vectors);
    UNUSED_ARG(myradius);
    UNUSED_ARG(myheight);
    // Flag that this is unknown at this point
    mytype = -1;
  };
};

} // NAMESPACE Geometry

} // NAMESPACE Mantid

#endif
