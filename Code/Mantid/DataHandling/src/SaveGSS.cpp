//---------------------------------------------------
// Includes
//---------------------------------------------------
#include "MantidDataHandling/SaveGSS.h"
#include "MantidKernel/UnitFactory.h"
#include "MantidKernel/FileValidator.h"
#include "MantidAPI/MatrixWorkspace.h"
#include "Poco/Timestamp.h"
#include "Poco/DateTimeFormatter.h"
#include <algorithm>
#include <fstream>
#include <iomanip>

using namespace Mantid::DataHandling;

// Register the algorithm into the AlgorithmFactory
DECLARE_ALGORITHM(SaveGSS)

//---------------------------------------------------
// Private member functions
//---------------------------------------------------
/**
 * Initialise the algorithm
 */
void SaveGSS::init()
{
  // Data must be in TOF
	declareProperty(new API::WorkspaceProperty<> ("InputWorkspace", "", Kernel::Direction::Input),
	    "The X values for the input workspace must be in units of wavelength");
  declareProperty("Filename", "",
    new Mantid::Kernel::FileValidator(std::vector<std::string>(), false),
    "The filename to use when saving data", Kernel::Direction::Input);
  std::vector<std::string> Split(2);
  Split[0] = "True";
  Split[1] = "False";
  declareProperty("SplitFiles", "True", new Kernel::ListValidator(Split),
    "Save each spectrum in a different file (default true)" );
  declareProperty("Bank",1);
}

/**
 * Execute the algorithm
 */
void SaveGSS::exec()
{
  using namespace Mantid::API;
  //Retrieve the input workspace
  MatrixWorkspace_const_sptr inputWS = getProperty("InputWorkspace");
  const int nHist=inputWS->getNumberHistograms();
  //const bool isHistogram = inputWS->isHistogramData();

  std::string filename = getProperty("Filename");
  std::size_t pos=filename.find_first_of(".");
  std::string ext;
  if (pos!=std::string::npos) //Remove the extension
  {
  	ext=filename.substr(pos+1,filename.npos);
  	filename=filename.substr(0,pos);
  }
  int bank=getProperty("Bank");
  std::string split=getProperty("SplitFiles");
  std::ostringstream number;
  std::fstream out;
   Progress p(this,0.2,1.0,nHist);
	for (int i=0;i<nHist;i++)
	{
		const std::vector<double>& X=inputWS->readX(i);
		const std::vector<double>& Y=inputWS->readY(i);
		const std::vector<double>& E=inputWS->readE(i);

		if (split=="False" && i==0) // Assign only one file
		{
			out.open((filename+'.'+ext).c_str(),std::ios::out);
			writeHeaders(out,inputWS);
		}
		else if (split=="True")//Several files will be created with names: filename-i.ext
		{
			number << "-" << i;
			out.open((filename+number.str()+"."+ext).c_str(),std::ios::out);
			number.str("");
			writeHeaders(out,inputWS);
		}

		{ // New scope
		if (!out.is_open())
		{
			g_log.information("Could not open filename: "+filename);
			throw std::runtime_error("Could not open filename: "+filename);
		}
		const int datasize = Y.size();
		double bc1=X[0]*32;
		double bc2=(X[1]-X[0])*32;
		// Logarithmic step
		double bc4=(X[1]-X[0])/X[0];
		out << "# Data for spectra :"<< i << std::endl;
		out << "BANK "
				<< std::fixed << std::setprecision(0) << bank // First bank should be 1 for GSAS
				<< std::fixed << " " << datasize
				<< std::fixed << " " << datasize
				<< std::fixed << " " << "RALF"
				<< std::fixed << " " << std::setprecision(0) << std::setw(8) << bc1
				<< std::fixed << " " << std::setprecision(0) << std::setw(8) << bc2
				<< std::fixed << " " << std::setprecision(0) << std::setw(8) << bc1
				<< std::fixed << " " << std::setprecision(5) << std::setw(7) << bc4
				<< " FXYE"<<std::endl;
    for (int j = 0; j < datasize; j++)
    {
      out << std::fixed << std::setprecision(5) << std::setw(15) << 0.5*(X[j]+X[j+1])
	        << std::fixed << std::setprecision(8) << std::setw(18) << Y[j]*X[j]*bc4
		      << std::fixed << std::setprecision(8) << std::setw(18) << E[j]*X[j]*bc4 << "\n";
    }
    } // End separate scope
    //Close at each iteration
  	if (split=="True")
    {
      out.close();
    }
	p.report();
  }
	// Close if single file
	if (split=="False")
  {
		out.close();
  }
	return;
}

/**
 * Write the header information for the given workspace
 * @param os The stream to use to write the information
 * @param workspace A shared pointer to MatrixWorkspace
 */
void SaveGSS::writeHeaders(std::ostream& os, Mantid::API::MatrixWorkspace_const_sptr& workspace) const
{
	os <<"# File generated by Mantid:" << std::endl;
	os <<"# Instrument: " << workspace->getBaseInstrument()->getName() << std::endl;

	return;
}

