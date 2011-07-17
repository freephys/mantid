#ifndef MANTID_MDALGORITHMS_MDPLANETEST_H_
#define MANTID_MDALGORITHMS_MDPLANETEST_H_

#include "MantidKernel/System.h"
#include "MantidKernel/Timer.h"
#include "MantidMDAlgorithms/MDPlane.h"
#include <cxxtest/TestSuite.h>
#include <iomanip>
#include <iostream>

using namespace Mantid;
using namespace Mantid::MDAlgorithms;
//using namespace Mantid::API;

class MDPlaneTest : public CxxTest::TestSuite
{
public:

  void test_constructor()
  {
    std::vector<coord_t> normal;
    std::vector<coord_t> point;
    TSM_ASSERT_THROWS_ANYTHING( "O-dimensions are not allowed.", MDPlane test(normal, point) );
    normal.push_back(1.234);
    normal.push_back(4.56);
    point.push_back(0);
    TSM_ASSERT_THROWS_ANYTHING( "Mismatched dimensions in normal/point are not allowed.", MDPlane test(normal, point) );
    point.push_back(0);
    MDPlane p(normal, point);
    TS_ASSERT_EQUALS( p.getNumDims(), 2);
    TS_ASSERT_DELTA( p.getNormal()[0], 1.234, 1e-5);
    TS_ASSERT_DELTA( p.getNormal()[1], 4.56,  1e-5);
    TS_ASSERT_DELTA( p.getInequality(), 0, 1e-5);
  }

  void test_constructor2()
  {
    coord_t normal[2] = {1.234, 4.56};
    coord_t point[2] = {1.0, 0.0};
    TSM_ASSERT_THROWS_ANYTHING( "O-dimensions are not allowed.", MDPlane test(0, normal, point) );
    MDPlane p(2, normal, point);
    TS_ASSERT_EQUALS( p.getNumDims(), 2);
    TS_ASSERT_DELTA( p.getNormal()[0], 1.234, 1e-5);
    TS_ASSERT_DELTA( p.getNormal()[1], 4.56,  1e-5);
    TS_ASSERT_DELTA( p.getInequality(), 1.234, 1e-5);
  }

  void test_copy_ctor()
  {
    coord_t normal[2] = {1.234, 4.56};
    coord_t point[2] = {1.0, 0.0};
    MDPlane p_orig(2, normal, point);
    MDPlane p(p_orig);
    TS_ASSERT_EQUALS( p.getNumDims(), 2);
    TS_ASSERT_DELTA( p.getNormal()[0], 1.234, 1e-5);
    TS_ASSERT_DELTA( p.getNormal()[1], 4.56,  1e-5);
    TS_ASSERT_DELTA( p.getInequality(), p_orig.getInequality(), 1e-5);
  }

  void test_assignment_operator()
  {
    coord_t normal[2] = {1.234, 4.56};
    coord_t point[2] = {1.0, 0.0};
    coord_t normal3[3] = {434, 456, 789};
    coord_t point3[3] = {1.0, 0.0, 0.0};
    MDPlane p_orig(2, normal, point);
    MDPlane p(3, normal3, point3);
    p = p_orig;
    TS_ASSERT_EQUALS( p.getNumDims(), 2);
    TS_ASSERT_DELTA( p.getNormal()[0], 1.234, 1e-5);
    TS_ASSERT_DELTA( p.getNormal()[1], 4.56,  1e-5);
    TS_ASSERT_DELTA( p.getInequality(), 1.234, 1e-5);
  }

  /// Helper function for the 2D case
  bool try2Dpoint(MDPlane & p, coord_t x, coord_t y)
  {
    coord_t centers[2] = {x,y};
    return p.isPointBounded(centers);
  }

  /// 2D test with some simple linear inequations
  void test_2D_point()
  {
    // Plane where x < 5
    coord_t normal1[2] = {-1., 0};
    coord_t point1[2] = {5., 0};
    MDPlane p1(2, normal1, point1);
    TS_ASSERT(  try2Dpoint(p1, 4.0, 12.) );
    TS_ASSERT( !try2Dpoint(p1, 6.0, -5.) );
    TS_ASSERT( !try2Dpoint(p1, 5.0, 1. ) );

    // Plane where x > 5
    coord_t normal2[2] = {+1., 0};
    MDPlane p2(2, normal2, point1);
    TS_ASSERT( !try2Dpoint(p2, 4.0, 12.) );
    TS_ASSERT(  try2Dpoint(p2, 6.0, -5.) );
    TS_ASSERT( !try2Dpoint(p2, 5.0, 1. ) );

    // Plane where y < 10
    coord_t normal3[2] = {0., -1.};
    coord_t point3[2] = {0., 10.};
    MDPlane p3(2, normal3, point3);
    TS_ASSERT(  try2Dpoint(p3, 100.,  9.0) );
    TS_ASSERT( !try2Dpoint(p3, -99., 11.0) );

    // Plane below a 45 degree line passing through (0,0)
    coord_t normal4[2] = {1., -1.};
    coord_t point4[2] = {0., 0.};
    MDPlane p4(2, normal4, point4);
    TS_ASSERT(  try2Dpoint(p4, 1., 0.1) );
    TS_ASSERT(  try2Dpoint(p4, 1., 0.9) );
    TS_ASSERT(  try2Dpoint(p4, 1., -5.) );
    TS_ASSERT( !try2Dpoint(p4, 1., 1.1) );
    TS_ASSERT( !try2Dpoint(p4, 0., 0.1) );

    // Plane above a 45 degree line passing through (0,2)
    coord_t normal5[2] = {-1., +1.};
    coord_t point5[2] = {0., 2.};
    MDPlane p5(2, normal5, point5);
    TS_ASSERT( !try2Dpoint(p5, 0., 1.99) );
    TS_ASSERT(  try2Dpoint(p5, 0., 2.01) );
    TS_ASSERT( !try2Dpoint(p5, 0.1,2.01) );
  }


  /// Helper function for the 2D case of a line intersecting the plane
  bool try2Dline(MDPlane & p, coord_t x1, coord_t y1, coord_t x2, coord_t y2)
  {
    coord_t centers1[2] = {x1,y1};
    coord_t centers2[2] = {x2,y2};
    return p.doesLineIntersect(centers1, centers2);
  }

  void test_2D_line()
  {
    // Plane where x < 5
    coord_t normal1[2] = {-1., 0};
    coord_t point1[2] = {5., 0};
    MDPlane p1(2, normal1, point1);
    TS_ASSERT(  try2Dline(p1,   1,2,     6,2) );
    TS_ASSERT(  try2Dline(p1, 10,12,   4.99,8) );
    TS_ASSERT( !try2Dline(p1, 5.01,2,  5.02,2) );
    TS_ASSERT( !try2Dline(p1, 4.99,2,  4.25,2) );

    // Plane below a 45 degree line passing through (0,0)
    coord_t normal4[2] = {1., -1.};
    coord_t point4[2] = {0., 0.};
    MDPlane p4(2, normal4, point4);
    TS_ASSERT(  try2Dline(p4,   0.1,0.0,   0.1,0.2));
    TS_ASSERT( !try2Dline(p4,   0.1,0.0,   0.3,0.2));
    TS_ASSERT(  try2Dline(p4,   0.1,0.2,   0.3,0.2));
  }

};



//=========================================================================================
class MDPlaneTestPerformance : public CxxTest::TestSuite
{
public:

  void test_3D_point()
  {
    coord_t normal[3] = {1.23, 2.34, 3.45};
    coord_t point[3] = {1,0,0};

    coord_t pointA[3] = {0.111, 0.222, 0.333};

    MDPlane p(3, normal, point);
    bool res = false;
    for (size_t i=0; i<5*1000000 /*5 million*/; i++)
    {
      res = p.isPointBounded(pointA);
      (void) res;
    }
    TS_ASSERT(res);
  }

  void test_4D_point()
  {
    coord_t normal[4] = {1.23, 2.34, 3.45, 4.56};
    coord_t point[4] = {1};

    coord_t pointA[4] = {0.111, 0.222, 0.333, 0.444};

    MDPlane p(4, normal, point);
    bool res = false;
    for (size_t i=0; i<5*1000000 /*5 million*/; i++)
    {
      res = p.isPointBounded(pointA);
      (void) res;
    }
    TS_ASSERT(res);
  }


  void test_3D_line()
  {
    coord_t normal[3] = {1.23, 2.34, 3.45};
    coord_t pointA[3] = {0.111, 0.222, 0.333};
    coord_t pointB[3] = {9.111, 9.222, 9.333};

//    MDPlane p(3, normal, 5.67);
//    bool res = false;
//    for (size_t i=0; i<5*1000000 /*5 million*/; i++)
//    {
//      res = p.doesLineIntersect(pointA, pointB);
//      (void) res;
//    }
//    TS_ASSERT(res);
  }

};

#endif /* MANTID_MDALGORITHMS_MDPLANETEST_H_ */

