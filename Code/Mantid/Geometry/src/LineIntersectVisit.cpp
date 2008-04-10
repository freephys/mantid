#include <fstream>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <cmath>
#include <list>
#include <stack>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <complex>
#include <boost/regex.hpp>
#include <boost/bind.hpp>

#include "MantidKernel/Logger.h"
#include "AuxException.h"
#include "XMLattribute.h"
#include "XMLobject.h"
#include "XMLgroup.h"
#include "XMLread.h"
#include "XMLcollect.h"
#include "IndexIterator.h"
#include "mathSupport.h"
#include "MantidKernel/Support.h"
#include "Matrix.h"
#include "Vec3D.h"
#include "BaseVisit.h"
#include "Surface.h"
#include "Quadratic.h"
#include "Plane.h"
#include "Cylinder.h"
#include "Cone.h"
#include "Sphere.h"
#include "General.h"
#include "Line.h"
#include "LineIntersectVisit.h"

namespace Mantid
{

namespace Geometry
{

Kernel::Logger& LineIntersectVisit::PLog(Kernel::Logger::get("LineIntersectVisit"));
LineIntersectVisit::LineIntersectVisit
  (const Geometry::Vec3D& Pt,const Geometry::Vec3D& uVec) :
    ATrack(Pt,uVec)
  /*!
    Constructor
  */
{}

void
LineIntersectVisit::Accept(const Surface&)
  /*!
    Process an intersect track
    \param :: Surface to use int line Interesect
  */
{
  throw ColErr::ExBase(-1,"LineIntersectVisit::Accept Surface");
  return;
}

void
LineIntersectVisit::Accept(const Quadratic& Surf)
  /*!
    Process an intersect track
    \param Surf :: Surface to use int line Interesect
  */
{
  ATrack.intersect(PtOut,Surf);
  procTrack();
  return;
}

void
LineIntersectVisit::Accept(const Plane& Surf)
  /*!
    Process an intersect track
    \param Surf :: Surface to use int line Interesect
  */
{
  ATrack.intersect(PtOut,Surf);
  procTrack();
  return;
}

void
LineIntersectVisit::Accept(const Cone& Surf)
  /*!
    Process an intersect track
    \param Surf :: Surface to use int line Interesect
  */
{
  ATrack.intersect(PtOut,Surf);
  procTrack();
  return;
}

void
LineIntersectVisit::Accept(const Cylinder& Surf)
  /*!
    Process an intersect track
    \param Surf :: Surface to use int line Interesect
  */
{
  ATrack.intersect(PtOut,Surf);
  procTrack();
  return;
}

void
LineIntersectVisit::Accept(const Sphere& Surf)
  /*!
    Process an intersect track
    \param Surf :: Surface to use int line Interesect
  */
{
  ATrack.intersect(PtOut,Surf);
  procTrack();
  return;
}

void
LineIntersectVisit::Accept(const General& Surf)
  /*!
    Process an intersect track
    \param Surf :: Surface to use int line Interesect
  */
{
  ATrack.intersect(PtOut,Surf);
  procTrack();
  return;
}

void
LineIntersectVisit::procTrack() 
  /*!
    Sorts the PtOut and distances
    with a closes first order.
  */
{
  // Calculate the distances to the points
  DOut.resize(PtOut.size());
  transform(PtOut.begin(),PtOut.end(),DOut.begin(),
	    boost::bind(&Geometry::Vec3D::Distance,ATrack.getOrigin(),_1));
  return;
}

}  // NAMESPACE MonteCarlo


}  // NAMESPACE Mantid
