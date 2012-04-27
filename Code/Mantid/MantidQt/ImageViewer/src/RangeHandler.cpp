
#include <iostream>
#include <QLineEdit>

#include "MantidQtImageViewer/RangeHandler.h"
#include "MantidQtImageViewer/QtUtils.h"
#include "MantidQtImageViewer/IVUtils.h"

namespace MantidQt
{
namespace ImageView
{

/**
 *  Construct a RangeHandler object to manage min, max and step controls 
 *  in the specified UI
 */
RangeHandler::RangeHandler( Ui_MainWindow* iv_ui )
{
  this->iv_ui = iv_ui;
}


/**
 * Configure the min, max and step controls for the specified data source.
 *
 * @param data_source  ImageDataSource that provides the data to be drawn
 */
void RangeHandler::ConfigureRangeControls( ImageDataSource* data_source )
{
  
  total_min_x   = data_source->GetXMin();
  total_max_x   = data_source->GetXMax();
  total_n_steps = data_source->GetNCols();

  double default_step = (total_max_x - total_min_x)/(double)total_n_steps;
  if ( total_n_steps > 2000 )
  {
    default_step = (total_max_x - total_min_x)/2000;
  }

  SetRange( total_min_x, total_max_x, default_step );
}


/**
 * Get the interval of values and the step size to use for rebinning the
 * spectra.  The range values are validated and adjusted if needed.  The
 * range values that are returned by this method will also be displayed in
 * the controls.
 *
 * @param min     This is the x value at the left edge of the first bin
 *                to display.
 * @param max     This is an x value at the right edge of the last bin
 *                to display.  This will be adjusted so that it is larger
 *                than min by an integer number of steps.  
 * @param step    This is size of the step to use between min and max.
 */
void RangeHandler::GetRange( double &min, double &max, double &step )
{
  QLineEdit* min_control  = iv_ui->x_min_input;
  QLineEdit* max_control  = iv_ui->x_max_input;
  QLineEdit* step_control = iv_ui->step_input;

  IVUtils::StringToDouble(  min_control->text().toStdString(), min );
  IVUtils::StringToDouble(  max_control->text().toStdString(), max );
  IVUtils::StringToDouble(  step_control->text().toStdString(), step );

  IVUtils::FindValidInterval( min, max );

  double max_steps = static_cast<double>(total_n_steps) * (max - min)/(total_max_x - total_min_x);
  if ( (max-min) / step > max_steps )
  {
    step = (total_max_x - total_min_x)/static_cast<double>(total_n_steps);
  } 

  SetRange( min, max, step );
}


/**
 * Adjust the values to be consistent with the avaliable data and 
 * diplay them in the controls.
 *
 * @param min     This is the x value at the left edge of the first bin.
 * @param max     This is an x value at the right edge of the last bin.
 * @param step    This is size of the step to use between min and max.
 */
void RangeHandler::SetRange( double min, double max, double step )
{
  IVUtils::FindValidInterval( min, max );

  if ( min < total_min_x )
  {
    min = total_min_x;
  }
  if ( max > total_max_x )
  {
    max = total_max_x;
  }

  if ( step < 0 )
  {
    step = -step;
  }

  if ( step == 0 )
  {
    step = (max-min)/(double)total_n_steps;
  }

  QtUtils::SetText( 7, 1, min, iv_ui->x_min_input );
  QtUtils::SetText( 7, 1, max, iv_ui->x_max_input );
  QtUtils::SetText( 7, 3, step, iv_ui->step_input );
}


} // namespace MantidQt 
} // namespace ImageView
