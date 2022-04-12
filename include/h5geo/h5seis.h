#ifndef H5SEIS_H
#define H5SEIS_H

#include "h5baseobject.h"

#include <Eigen/Dense>

#ifndef _USE_MATH_DEFINES
#define _USE_MATH_DEFINES   // should be before <cmath>, include 'pi' val
#endif
#include <math.h>

class H5SeisContainer;

class H5Seis : public H5BaseObject
{
protected:
  virtual ~H5Seis() = default;

public:

  // WRITERS
  virtual bool readSEGYTextHeader(const std::string& segy) = 0;
  virtual bool readSEGYBinHeader(const std::string& segy) = 0;
  virtual bool readSEGYTraces(
      const std::vector<std::string>& segyFiles,
      size_t trcBuffer = 10000) = 0;

  virtual bool writeTextHeader(const char (&txtHdr)[40][80]) = 0;

  /// \brief writeTextHeader Max 40x80 chars are to be written
  /// \param txtHdr
  /// \return
  virtual bool writeTextHeader(const std::vector<std::string>& txtHdr) = 0;
  virtual bool writeBinHeader(const double (&binHdr)[30]) = 0;

  /// \brief writeBinHeader Vector length should be equal to getNBinHdr
  /// \param binHdrVec
  /// \return
  virtual bool writeBinHeader(const std::vector<double>& binHdrVec) = 0;
  virtual bool writeBinHeader(
      const Eigen::Ref<const Eigen::VectorXd>& binHdrVec) = 0;
  virtual bool writeBinHeader(
      const std::string& hdrName,
      const double& value,
      const std::string& unitsFrom = "",
      const std::string& unitsTo = "") = 0;
  virtual bool writeBoundary(
      Eigen::Ref<Eigen::MatrixX2d> M,
      const std::string& lengthUnits = "",
      bool doCoordTransform = false) = 0;
  virtual bool writeTrace(
      const Eigen::Ref<const Eigen::MatrixXf>& TRACE,
      const size_t& fromTrc = 0,
      const size_t& fromSampInd = 0) = 0;
  virtual bool writeTraceHeader(
      const Eigen::Ref<const Eigen::MatrixXd>& HDR,
      const size_t& fromTrc = 0,
      const size_t& fromHdrInd = 0) = 0;
  virtual bool writeTraceHeader(
      const std::string& hdrName,
      Eigen::Ref<Eigen::MatrixXd> hdr,
      const size_t& fromTrc = 0,
      const std::string& unitsFrom = "",
      const std::string& unitsTo = "") = 0;
  virtual bool writeTraceHeader(
      const std::string& hdrName,
      Eigen::Ref<Eigen::MatrixXd> hdr,
      const Eigen::Ref<const Eigen::VectorX<size_t>>& trcInd,
      const std::string& unitsFrom = "",
      const std::string& unitsTo = "") = 0;

  virtual bool writeXYTraceHeaders(
      const std::vector<std::string>& xyHdrNames,
      Eigen::Ref<Eigen::MatrixXd>& xy,
      const size_t& fromTrc = 0,
      const std::string& lengthUnits = "",
      bool doCoordTransform = false) = 0;
  virtual bool writeXYTraceHeaders(
      const std::vector<std::string>& xyHdrNames,
      Eigen::Ref<Eigen::MatrixXd>& xy,
      const Eigen::Ref<const Eigen::VectorX<size_t>>& trcInd,
      const std::string& lengthUnits = "",
      bool doCoordTransform = false) = 0;

  /// resize trace and trace header datasets
  virtual bool setNTrc(size_t nTrc) = 0;
  /// resize trace datasets
  virtual bool setNSamp(size_t nSamp) = 0;

  // GETTERS
  virtual std::vector<std::string> getTextHeader() = 0;
  virtual std::map<std::string, double> getBinHeader() = 0;
  virtual double getBinHeader(
      const std::string& hdrName,
      const std::string& unitsFrom = "",
      const std::string& unitsTo = "") = 0;

  /// \brief getTrace Get block of traces. If `nTrc` or
  /// `nSamp` exceed max values then these values are
  /// changed to max allowed (that is why they are not `const`)
  /// \param fromTrc
  /// \param nTrc
  /// \param fromSampInd
  /// \param nSamp
  /// \param dataUnits
  /// \return
  virtual Eigen::MatrixXf getTrace(
      const size_t& fromTrc,
      size_t nTrc = 1,
      const size_t& fromSampInd = 0,
      size_t nSamp = std::numeric_limits<size_t>::max(),
      const std::string& dataUnits = "") = 0;

  /// \brief getTraceHeader Get block of trace headers.
  /// If `nTrc` or `nHdr` exceed max values then these
  /// values are changed to max allowed (that is why
  /// they are not `const`)
  /// \param fromTrc
  /// \param nTrc
  /// \param fromHdr
  /// \param nHdr
  /// \param unitsFrom
  /// \param unitsTo
  /// \return
  virtual Eigen::MatrixXd getTraceHeader(
      const size_t& fromTrc,
      size_t nTrc = 1,
      const size_t& fromHdr = 0,
      size_t nHdr = std::numeric_limits<size_t>::max(),
      const std::vector<std::string>& unitsFrom = std::vector<std::string>(),
      const std::vector<std::string>& unitsTo = std::vector<std::string>()) = 0;
  virtual Eigen::VectorXd getTraceHeader(
      const std::string& hdrName,
      const size_t& fromTrc = 0,
      const size_t& nTrc = 1,
      const std::string& unitsFrom = "",
      const std::string& unitsTo = "") = 0;
  virtual Eigen::MatrixXd getTraceHeader(
      const std::vector<size_t>& trcInd,
      const std::vector<size_t>& trcHdrInd,
      const std::vector<std::string>& unitsFrom = std::vector<std::string>(),
      const std::vector<std::string>& unitsTo = std::vector<std::string>()) = 0;
  virtual Eigen::MatrixXd getTraceHeader(
      const Eigen::Ref<const Eigen::VectorX<size_t>>& trcInd,
      const Eigen::Ref<const Eigen::VectorX<size_t>>& trcHdrInd,
      const std::vector<std::string>& unitsFrom = std::vector<std::string>(),
      const std::vector<std::string>& unitsTo = std::vector<std::string>()) = 0;
  virtual Eigen::MatrixXd getTraceHeader(
      const std::vector<std::string>& hdrNames,
      const std::vector<size_t>& trcInd,
      const std::vector<std::string>& unitsFrom = std::vector<std::string>(),
      const std::vector<std::string>& unitsTo = std::vector<std::string>()) = 0;
  virtual Eigen::MatrixXd getTraceHeader(
      const std::vector<std::string>& hdrNames,
      const Eigen::Ref<const Eigen::VectorX<size_t>>& trcInd,
      const std::vector<std::string>& unitsFrom = std::vector<std::string>(),
      const std::vector<std::string>& unitsTo = std::vector<std::string>()) = 0;

  /// Do the same as `getTraceHeader()` but also able to do a coord transform.
  /// \return two column matrix if successful. Otherwise empty matrix is returned
  virtual Eigen::MatrixXd getXYTraceHeaders(
      const std::vector<std::string>& xyHdrNames,
      const size_t& fromTrc = 0,
      size_t nTrc = std::numeric_limits<size_t>::max(),
      const std::string& lengthUnits = "",
      bool doCoordTransform = false) = 0;
  virtual Eigen::MatrixXd getXYTraceHeaders(
      const std::vector<std::string>& xyHdrNames,
      const Eigen::Ref<const Eigen::VectorX<size_t>>& trcInd,
      const std::string& lengthUnits = "",
      bool doCoordTransform = false) = 0;


  /// \brief readSortedData Get sorted data based on precalculated
  /// primary sort keys (e.g. before using it you should prepare
  /// primary sort keys with `addPKeySort(...)` method)
  /// \param TRACE this is not Eigen::Ref<> because Eigen::Ref<>
  /// doesn't allow to resize matrices
  /// \param HDR this is not Eigen::Ref<> because Eigen::Ref<>
  /// doesn't allow to resize matrices
  /// \param keyList
  /// \param minList
  /// \param maxList
  /// \param fromSampInd first sample index to read
  /// (from 0 to getNSamp())
  /// \param nSamp Number of samples to read (if 0 then
  /// 'TRACE' will be empty). By default all samples
  /// \param readTraceByTrace whether to read h5 in row or col order
  /// \param dataUnits you will get data transformed to these units
  /// \param lengthUnits works only in pair with 'doCoordTransform'
  /// \param doCoordTransform only works if two header names are passed (X and Y)
  /// \return vector of trace indexes read
  virtual Eigen::VectorX<size_t> getSortedData(
      Eigen::MatrixXf& TRACE,
      Eigen::MatrixXd& HDR,
      const std::vector<std::string>& keyList,
      const std::vector<double>& minList,
      const std::vector<double>& maxList,
      size_t fromSampInd = 0,
      size_t nSamp = std::numeric_limits<size_t>::max(),
      bool readTraceByTrace = true,
      const std::string& dataUnits = "",
      const std::string& lengthUnits = "",
      bool doCoordTransform = false) = 0;

  virtual ptrdiff_t getBinHeaderIndex(const std::string& hdrName) = 0;
  virtual ptrdiff_t getTraceHeaderIndex(const std::string& hdrName) = 0;

  virtual Eigen::VectorXd getSamples(
      const size_t& trcInd,
      const std::string& units = "") = 0;
  virtual double getFirstSample(
      const size_t& trcInd,
      const std::string& units = "") = 0;
  virtual double getLastSample(
      const size_t& trcInd,
      const std::string& units = "") = 0;
  virtual double getSampRate(
      const std::string& units = "") = 0;
  virtual size_t getNSamp() = 0;
  virtual size_t getNTrc() = 0;
  /*! usually 78 !*/
  virtual size_t getNTrcHdr() = 0;
  virtual size_t getNBinHdr() = 0;
  virtual size_t getNTextHdrRows() = 0;
  virtual Eigen::VectorX<size_t> getPKeyIndexes(
      const std::string& pKey,
     double pMin, double pMax) = 0;
  virtual Eigen::VectorXd getPKeyValues(
      const std::string& pKey,
      const std::string& unitsFrom = "",
      const std::string& unitsTo = "") = 0;
  /// Return number unique values of given pKey
  virtual size_t getPKeySize(const std::string& pKey) = 0;
  /// Return number of traces to be selected of given pKey
  virtual size_t getPKeyTraceSize(const std::string& pKey, double pMin, double pMax) = 0;
  virtual std::vector<std::string> getPKeyNames() = 0;
  virtual std::map<std::string, double> getTraceHeaderMin() = 0;
  virtual std::map<std::string, double> getTraceHeaderMax() = 0;
  virtual double getTraceHeaderMin(
      const std::string& hdrName,
      const std::string& unitsFrom = "",
      const std::string& unitsTo = "") = 0;
  virtual double getTraceHeaderMax(
      const std::string& hdrName,
      const std::string& unitsFrom = "",
      const std::string& unitsTo = "") = 0;

  virtual SeisParam getParam() = 0;

  /// \brief checkTraceLimits check *fromTrc*, *nTrc* and diminish
  ///  *nTrc* to fit in data limits (if *fromTrc* is inside limit)
  /// \param fromTrc first trace (to read for example)
  /// \param nTrc number of trace (to read for example)
  /// \return
  virtual bool checkTraceLimits(
      const size_t& fromTrc, size_t& nTrc) = 0;

  /// \brief checkTraceHeaderLimits check 'fromHdr' and 'nHdr' and diminish
  /// 'nHdr' to fit in data limits (if 'fromTrc' is inside limit)
  /// \param fromHdr first header (usually there are 78 headers so
  /// the value should be less then this value)
  /// \param nHdr number of headers (to read for example)
  /// \return
  virtual bool checkTraceHeaderLimits(
      const size_t& fromHdr, size_t& nHdr) = 0;
  virtual bool checkSampleLimits(
      const size_t& fromSampInd, size_t& nSamp) = 0;

  virtual bool generatePRESTKGeometry(
      double src_x0, double src_dx, size_t src_nx,
      double src_y0, double src_dy, size_t src_ny,
      double src_z,
      double rec_x0, double rec_dx, size_t rec_nx,
      double rec_y0, double rec_dy, size_t rec_ny,
      double rec_z,
      bool moveRec,
      const std::string& lengthUnits = "",
      bool doCoordTransform = false) = 0;
  virtual bool generateSTKGeometry(
      double x0, double dx, size_t nx,
      double y0, double dy, size_t ny,
      double z,
      const std::string& lengthUnits = "",
      bool doCoordTransform = false) = 0;

  virtual bool setDomain(const h5geo::Domain& domain) = 0;
  virtual bool setDataType(const h5geo::SeisDataType& seisType) = 0;
  virtual bool setSurveyType(const h5geo::SurveyType& surveyType) = 0;
  virtual bool setSRD(double val, const std::string& lengthUnits = "") = 0;
  virtual bool setSampRate(double val, const std::string& units = "") = 0;
  virtual bool setFirstSample(double val, const std::string& units = "") = 0;

  virtual h5geo::Domain getDomain() = 0;
  virtual h5geo::SeisDataType getDataType() = 0;
  virtual h5geo::SurveyType getSurveyType() = 0;
  virtual double getSRD(const std::string& lengthUnits = "") = 0;
  virtual Eigen::MatrixXd getBoundary(
      const std::string& lengthUnits = "",
      bool doCoordTransform = false) = 0;

  virtual bool hasPKeySort(const std::string& pKeyName) = 0;
  virtual bool removePKeySort(const std::string& pKeyName) = 0;
  virtual bool addPKeySort(const std::string& pKeyName) = 0;

  virtual H5SeisContainer* openSeisContainer() = 0;

  virtual std::optional<h5gt::DataSet> getBoundaryD() = 0;
  virtual std::optional<h5gt::DataSet> getTextHeaderD() = 0;
  virtual std::optional<h5gt::DataSet> getBinHeaderD() = 0;
  virtual std::optional<h5gt::DataSet> getTraceHeaderD() = 0;
  virtual std::optional<h5gt::DataSet> getTraceD() = 0;
  virtual std::optional<h5gt::Group> getSortG() = 0;
  virtual std::optional<h5gt::Group> getUValG() = 0;
  virtual std::optional<h5gt::Group> getIndexesG() = 0;

  virtual std::optional<h5gt::Group> getSEGYG() = 0;
  virtual std::optional<h5gt::DataSet> getSEGYTextHeaderD() = 0;
  virtual std::optional<h5gt::DataSet> getSEGYBinHeader2BytesD() = 0;
  virtual std::optional<h5gt::DataSet> getSEGYBinHeader4BytesD() = 0;
  virtual std::optional<h5gt::DataSet> getSEGYTraceHeader2BytesD() = 0;
  virtual std::optional<h5gt::DataSet> getSEGYTraceHeader4BytesD() = 0;
  virtual std::optional<h5gt::DataSet> getSEGYTraceFloatD() = 0;

  /// Calculate and write min/max trace headers
  virtual bool updateTraceHeaderLimits(size_t nTrcBuffer = 1e7) = 0;
  /// Calculate and write XY boundary based on CDP_X and CDP_Y
  virtual bool updateBoundary() = 0;
  virtual bool updatePKeySort(const std::string& pKeyName) = 0;
};

namespace h5geo {
  extern "C" {
  H5GEO_EXPORT H5Seis* openSeis(h5gt::Group group);
  }
}

using H5Seis_ptr = std::unique_ptr<H5Seis, h5geo::ObjectDeleter>;

#endif // H5SEIS_H
