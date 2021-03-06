#ifndef CACHE_GEOMETRYHANDLER_H
#define CACHE_GEOMETRYHANDLER_H

#include "MantidGeometry/DllConfig.h"
#include "MantidGeometry/Rendering/GeometryHandler.h"

namespace Mantid {
namespace Kernel {
class V3D;
}

namespace Geometry {
class GeometryHandler;
class CacheGeometryRenderer;
class CacheGeometryGenerator;
class IObjComponent;
class CSGObject;

/**
   \class CacheGeometryHandler
   \brief Place holder for geometry triangulation and rendering with caching
   triangles.
   \author Srikanth Nagella
   \date Jan 2009
   \version 1.0

   This is an implementation class for handling geometry from cache, if the
   cache doesn't exist then the
   triangulation is done using another triangulation handler and store in cache.

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
class MANTID_GEOMETRY_DLL CacheGeometryHandler : public GeometryHandler {
private:
  CacheGeometryRenderer *Renderer; ///< Geometry renderer variable used for
  /// rendering Object/ObjComponent
  CacheGeometryGenerator *
      Triangulator; ///< Geometry generator to triangulate Object

public:
  CacheGeometryHandler(IObjComponent *comp);              ///< Constructor
  CacheGeometryHandler(boost::shared_ptr<CSGObject> obj); ///< Constructor
  CacheGeometryHandler(CSGObject *obj);                   ///< Constructor
  boost::shared_ptr<GeometryHandler> clone() const override;
  ~CacheGeometryHandler() override; ///< Destructor
  GeometryHandler *createInstance(IObjComponent *comp) override;
  GeometryHandler *createInstance(boost::shared_ptr<CSGObject> obj) override;
  GeometryHandler *createInstance(CSGObject *obj) override;

  void Triangulate() override;
  void Render() override;
  void Initialize() override;
  bool canTriangulate() override { return true; }
  int NumberOfTriangles() override;
  int NumberOfPoints() override;
  double *getTriangleVertices() override;
  int *getTriangleFaces() override;
  /// Sets the geometry cache using the triangulation information provided
  void setGeometryCache(int noPts, int noFaces, double *pts,
                        int *faces) override;
};

} // NAMESPACE Geometry

} // NAMESPACE Mantid

#endif
