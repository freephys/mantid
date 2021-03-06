==========================
Indirect Inelastic Changes
==========================

.. contents:: Table of Contents
   :local:

Algorithms
----------

New
###

- :ref:`algm-ExtractQENSMembers` can be used to extract the fit members from any QENS fit.
- New algorithm :ref:`BASISDiffraction <algm-BASISDiffraction-v1>` to determine the orientation of crystal samples for the BASIS beamline.


Improved
########

- :ref:`algm-ApplyPaalmanPingsCorrection` now accepts a corrections group containing only an :math:`A_{s,s}` and an :math:`A_{c,c}` workspace (produced by :ref:`algm-CalculateMonteCarloAbsorption`).
- :ref:`BASISReduction  <algm-BASISReduction>` now permits the user to exclude a contiguous time segment from the reduction process.
- :ref:`BASISReduction <algm-BASISReduction>` option *noMonitorNorm* changed to *MonitorNorm*.
- :ref:`BASISReduction <algm-BASISReduction>` now contains log entry *asString* storing the options passed to to the algorithm.
- :ref:`IqtFitSequential <algm-IqtFitSequential>` and `IqtFitMultiple <algm-IqtFitMultiple>` can now both extract members from the fit (when the ExtractMembers property is set to True).

Vesuvio
-------

New
###
- Cumulative Angle-Averaged Data (sum of fits normalised by their integral) can be calculated and produced as output by setting the 'calculate_caad' flag to True.

Improved
########
- A pre-loaded runs workspace can now be passed to the fit_tof VESUVIO routine, which will skip the loading subroutine given this input
- Loading the sample log files into a workspace can be disabled when calling the :ref:`LoadVesuvio <algm-LoadVesuvio>` algorithm by supplying `LoadLogFiles=False` to the algorithm call
- Loading the sample log files into a workspace can be disabled within a Vesuvio Driver Script, by setting the 'load_log_files' flag to False

Bugfixes
########
- Previously, running a script which only applied a single correction (e.g. container subtraction), would produce an error 'f0.Scaling', this has now been fixed.

Data Analysis Interfaces
------------------------

New
###
- ConvFit, IqtFit, MSDFit and JumpFit now have a second mini-plot for the difference. The sample and calculated fit are found in the top mini-plot, the difference is found in the bottom mini-plot.
- The function browser in each of the Fitting tabs (ConvFit, IqtFit, MSDFit, JumpFit) has been replaced with a new IndirectFitPropertyBrowser widget (which can be separated and embedded into the fit interfaces).
- The IndirectFitPropertyBrowser widgets provides the following new functionality:
  - Ties can now be used to tie parameters between all functions and custom ties (involving mathematical expressions) are now available.
  - It is now possible to add constraints to parameters.
  - Any additional functions can be added from the library of available MANTID functions by right-clicking and selecting 'Add Function'.
  - Function setups can now be saved and re-loaded (Custom Setups).
  - Right-clicking on function in the browser and selecting 'Help' will bring up the documentation of that function.
  - Functions can be copied and loaded from the clipboard.

Improved
########
- The Plot Guess Feature in the ConvFit Interface is now enabled for the diffusion functions.
- The Plot Guess Feature in the MSDFit Interface is now implemented for the three models introduced in release v3.11 (MsdGauss, MsdPeters and MsdYi).
- The ExtractMembers option in the ConvFit Interface will now function correctly for diffusion functions.
- The ExtractMembers option is now available in the IqtFit interface.

Bugfixes
########
- The X-Limits for all of the Indirect Data Analysis interfaces are now correctly updated when data is loaded.
- In the IqtFit interface, the 'AO' parameter now defaults to 0.
- The mini preview plot now updates correctly in the Indirect Data Analysis interfaces, when the fit function is changed; when changed to a function that wasn't used in the most recent fit, will plot only the sample, else will plot the sample, fit and difference.
- Plotting individual parameters of the fit in the interface ('Plot Options'), will no longer produce an error in the ConvFit interface, when plotting 'FWHM'.
- In the Calculate Paalman Pings tab of the Indirect Correction interface the container back thickness is now set correctly.


Indirect Diffraction
--------------------

Improved
########
- Manual D-Range option removed from the indirect diffraction reduction interface; D-Ranges are now automatically calculated for sample, container and vanadium runs.

Corrections Interfaces
----------------------

Improved
########
- The Apply Paalman Pings interface has been renamed to Apply Absorption Correction.
- The Apply Absorption Correction interface no longer requires workspaces to be in units of wavelength (this is done within :ref:`algm-ApplyPaalmanPingsCorrection`).

Abins
-----

Improved
########
- Performance of Abins routines significantly improved (a factor of 10-20 times for data size of 4000).

:ref:`Release 3.12.0 <v3.12.0>`
