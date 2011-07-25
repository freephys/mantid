#ifndef MANTID_MDEVENTS_COORDTRANSFORMDISTANCEPARSER_H_
#define MANTID_MDEVENTS_COORDTRANSFORMDISTANCEPARSER_H_

#include "MantidKernel/System.h"
#include <boost/shared_ptr.hpp>
#include "MantidMDEvents/CoordTransformParser.h"

namespace Mantid
{
  namespace MDEvents
  {
    /// Forward declaration
    class CoordTransformDistance;

    /** A parser for processing coordinate transform xml
   *
   * @author Owen Arnold
   * @date 25/july/2011
   */
    class DLLExport CoordTransformDistanceParser : public CoordTransformParser
    {
    public:
      CoordTransformDistanceParser();
      virtual CoordTransform* createTransform(Poco::XML::Element* coordTransElement) const;
      virtual ~CoordTransformDistanceParser();
    private:
      CoordTransformDistanceParser(const CoordTransformDistanceParser&);
      CoordTransformDistanceParser& operator=(const CoordTransformDistanceParser&);
    };
  }
}

#endif