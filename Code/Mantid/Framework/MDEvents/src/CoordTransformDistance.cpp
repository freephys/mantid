#include "MantidKernel/Exception.h"
#include "MantidKernel/System.h"
#include "MantidKernel/System.h"
#include "MantidMDEvents/CoordTransform.h"
#include "MantidMDEvents/CoordTransformDistance.h"

#include <boost/algorithm/string.hpp>
#include <boost/format.hpp>

using namespace Mantid::Geometry;
using namespace Mantid::Kernel;

namespace Mantid
{
namespace MDEvents
{


  //----------------------------------------------------------------------------------------------
  /** Constructor
   *
   * @param inD :: # of input dimensions
   * @param center :: array of size[inD], with the coordinates at the center
   * @param dimensionsUsed :: bool array of size[inD] where True is set for those dimensions that are considered when
   *        calculating distance.
   * @return
   */
  CoordTransformDistance::CoordTransformDistance(const size_t inD, const coord_t * center, const bool * dimensionsUsed)
  : CoordTransform(inD, 1), m_center(inD), m_dimensionsUsed(inD)
  {
    // Create and copy the arrays.
    for (size_t d=0; d<inD; d++)
    {
      m_center.addValue(d, center[d]);
      m_dimensionsUsed.addValue(d, dimensionsUsed[d]);
    }
  }
    
  //----------------------------------------------------------------------------------------------
  /** Destructor
   */
  CoordTransformDistance::~CoordTransformDistance()
  {
  }
  

  //----------------------------------------------------------------------------------------------
  /** Apply the coordinate transformation.
   *
   * Calculate the SQUARE of the distance between the input coordinates to m_center
   * but only on dimensionsUsed[d] == true.
   *
   * @param inputVector :: fixed-size array of input coordinates, of size inD
   * @param outVector :: fixed-size array of output coordinates, of size 1
   */
  void CoordTransformDistance::apply(const coord_t * inputVector, coord_t * outVector)
  {
    coord_t distanceSquared = 0;
    for (size_t d=0; d<inD.getValue(); d++)
    {
      if (true == m_dimensionsUsed[d])
      {
        coord_t dist = inputVector[d] - m_center[d];
        distanceSquared += (dist * dist);
      }
    }
    /// Return the only output dimension
    outVector[0] = distanceSquared;
  }

  //----------------------------------------------------------------------------------------------
  /** Serialize the coordinate transform distance
  *
  * @return The coordinate transform distance in its serialized form.
  */
  std::string CoordTransformDistance::toXMLString() const
  {
     using namespace Poco::XML;

      AutoPtr<Document> pDoc = new Document;
      AutoPtr<Element> functionElement = pDoc->createElement("CoordTransformDistance");
      pDoc->appendChild(functionElement);

      AutoPtr<Element> paramListElement = pDoc->createElement("ParameterList");

      AutoPtr<Text> formatText = pDoc->createTextNode("%s%s%s%s");
      paramListElement->appendChild(formatText);
      functionElement->appendChild(paramListElement);

      std::stringstream xmlstream;

      DOMWriter writer;
      writer.writeNode(xmlstream, pDoc);

      std::string formattedXMLString = boost::str(boost::format(xmlstream.str().c_str())
        % inD.toXMLString().c_str() 
        % outD.toXMLString().c_str() 
        % m_center.toXMLString().c_str()
        % m_dimensionsUsed.toXMLString().c_str());

      return formattedXMLString;
  }

} // namespace Mantid
} // namespace MDEvents

