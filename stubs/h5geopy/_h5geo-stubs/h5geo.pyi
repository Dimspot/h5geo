"""API to work with geo-data (seismic, wells, surfaces, other in process) based on HDF5 and originally written in C++: https://github.com/tierra-colada/h5geo"""
import h5geopy._h5geo
import typing
import h5gtpy._h5gt
import numpy
import sys
_Shape = typing.Tuple[int, ...]

__all__ = [
    "AngleUnits",
    "CaseSensitivity",
    "ContainerType",
    "CreationType",
    "Delimiter",
    "DevCurveParam",
    "DevDataType",
    "Domain",
    "H5Base",
    "H5BaseContainer",
    "H5BaseObject",
    "H5DevCurve",
    "H5LogCurve",
    "H5Seis",
    "H5SeisContainer",
    "H5Surf",
    "H5SurfContainer",
    "H5Well",
    "H5WellContainer",
    "LogCurveParam",
    "LogDataType",
    "MdAzIncl2ALL",
    "MdAzIncl2MdXYTvd",
    "ObjectType",
    "SegyEndian",
    "SegyFormat",
    "SeisDataType",
    "SeisParam",
    "SpatialUnits",
    "SurfParam",
    "SurveyType",
    "TemporalUnits",
    "TrajectoryFormat",
    "TvdDxDy2ALL",
    "TvdDxDy2MdAzIncl",
    "TvdDxDy2MdXYTvd",
    "TvdXY2ALL",
    "TvdXY2MdAzIncl",
    "TvdXY2MdXYTvd",
    "TvdssDxDy2ALL",
    "TvdssDxDy2MdAzIncl",
    "TvdssDxDy2MdXYTvd",
    "TvdssXY2ALL",
    "TvdssXY2MdAzIncl",
    "TvdssXY2MdXYTvd",
    "TxtEncoding",
    "WellDataType",
    "WellName",
    "WellParam",
    "WellType",
    "createSeisContainer",
    "createSeisContainerByName",
    "createSurfContainer",
    "createSurfContainerByName",
    "createWellContainer",
    "createWellContainerByName",
    "openBaseContainer",
    "openBaseContainerByName",
    "openBaseObject",
    "openSeisContainer",
    "openSeisContainerByName",
    "openSurfContainerByName",
    "openWellContainer",
    "openWellContainerByName",
    "quickHull2D",
    "sort",
    "sort_rows",
    "sort_rows_unique",
    "sort_unique"
]


class AngleUnits():
    """
    Members:

      DEGREE

      RADIAN
    """
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __gt__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    DEGREE: h5geopy._h5geo.AngleUnits # value = <AngleUnits.DEGREE: 0>
    RADIAN: h5geopy._h5geo.AngleUnits # value = <AngleUnits.RADIAN: 1>
    __members__: dict # value = {'DEGREE': <AngleUnits.DEGREE: 0>, 'RADIAN': <AngleUnits.RADIAN: 1>}
    pass
class CaseSensitivity():
    """
    Members:

      CASE_SENSITIVE

      CASE_INSENSITIVE
    """
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __gt__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    CASE_INSENSITIVE: h5geopy._h5geo.CaseSensitivity # value = <CaseSensitivity.CASE_INSENSITIVE: 2>
    CASE_SENSITIVE: h5geopy._h5geo.CaseSensitivity # value = <CaseSensitivity.CASE_SENSITIVE: 1>
    __members__: dict # value = {'CASE_SENSITIVE': <CaseSensitivity.CASE_SENSITIVE: 1>, 'CASE_INSENSITIVE': <CaseSensitivity.CASE_INSENSITIVE: 2>}
    pass
class ContainerType():
    """
    Members:

      SURFACE

      WELL

      SEISMIC
    """
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __gt__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    SEISMIC: h5geopy._h5geo.ContainerType # value = <ContainerType.SEISMIC: 3>
    SURFACE: h5geopy._h5geo.ContainerType # value = <ContainerType.SURFACE: 1>
    WELL: h5geopy._h5geo.ContainerType # value = <ContainerType.WELL: 2>
    __members__: dict # value = {'SURFACE': <ContainerType.SURFACE: 1>, 'WELL': <ContainerType.WELL: 2>, 'SEISMIC': <ContainerType.SEISMIC: 3>}
    pass
class CreationType():
    """
    Members:

      OPEN_OR_CREATE

      CREATE_OR_OVERWRITE

      CREATE_UNDER_NEW_NAME
    """
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __gt__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    CREATE_OR_OVERWRITE: h5geopy._h5geo.CreationType # value = <CreationType.CREATE_OR_OVERWRITE: 2>
    CREATE_UNDER_NEW_NAME: h5geopy._h5geo.CreationType # value = <CreationType.CREATE_UNDER_NEW_NAME: 3>
    OPEN_OR_CREATE: h5geopy._h5geo.CreationType # value = <CreationType.OPEN_OR_CREATE: 1>
    __members__: dict # value = {'OPEN_OR_CREATE': <CreationType.OPEN_OR_CREATE: 1>, 'CREATE_OR_OVERWRITE': <CreationType.CREATE_OR_OVERWRITE: 2>, 'CREATE_UNDER_NEW_NAME': <CreationType.CREATE_UNDER_NEW_NAME: 3>}
    pass
class Delimiter():
    """
    Members:

      TABULATION

      SEMICOLON

      DOT

      SPACE

      COMMA
    """
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __gt__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    COMMA: h5geopy._h5geo.Delimiter # value = <Delimiter.COMMA: 16>
    DOT: h5geopy._h5geo.Delimiter # value = <Delimiter.DOT: 4>
    SEMICOLON: h5geopy._h5geo.Delimiter # value = <Delimiter.SEMICOLON: 2>
    SPACE: h5geopy._h5geo.Delimiter # value = <Delimiter.SPACE: 8>
    TABULATION: h5geopy._h5geo.Delimiter # value = <Delimiter.TABULATION: 1>
    __members__: dict # value = {'TABULATION': <Delimiter.TABULATION: 1>, 'SEMICOLON': <Delimiter.SEMICOLON: 2>, 'DOT': <Delimiter.DOT: 4>, 'SPACE': <Delimiter.SPACE: 8>, 'COMMA': <Delimiter.COMMA: 16>}
    pass
class DevCurveParam():
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, spatialUnits: SpatialUnits, temporalUnits: TemporalUnits, angleUnits: AngleUnits, setActive: bool = False, chunkSize: int = 1000) -> None: ...
    @property
    def angleUnits(self) -> AngleUnits:
        """
        :type: AngleUnits
        """
    @angleUnits.setter
    def angleUnits(self, arg0: AngleUnits) -> None:
        pass
    @property
    def chunkSize(self) -> int:
        """
        :type: int
        """
    @chunkSize.setter
    def chunkSize(self, arg0: int) -> None:
        pass
    @property
    def setActive(self) -> bool:
        """
        :type: bool
        """
    @setActive.setter
    def setActive(self, arg0: bool) -> None:
        pass
    @property
    def spatialUnits(self) -> SpatialUnits:
        """
        :type: SpatialUnits
        """
    @spatialUnits.setter
    def spatialUnits(self, arg0: SpatialUnits) -> None:
        pass
    @property
    def temporalUnits(self) -> TemporalUnits:
        """
        :type: TemporalUnits
        """
    @temporalUnits.setter
    def temporalUnits(self, arg0: TemporalUnits) -> None:
        pass
    pass
class DevDataType():
    """
    Members:

      MD

      X

      Y

      TVD

      OWT
    """
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __gt__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    MD: h5geopy._h5geo.DevDataType # value = <DevDataType.MD: 1>
    OWT: h5geopy._h5geo.DevDataType # value = <DevDataType.OWT: 5>
    TVD: h5geopy._h5geo.DevDataType # value = <DevDataType.TVD: 4>
    X: h5geopy._h5geo.DevDataType # value = <DevDataType.X: 2>
    Y: h5geopy._h5geo.DevDataType # value = <DevDataType.Y: 3>
    __members__: dict # value = {'MD': <DevDataType.MD: 1>, 'X': <DevDataType.X: 2>, 'Y': <DevDataType.Y: 3>, 'TVD': <DevDataType.TVD: 4>, 'OWT': <DevDataType.OWT: 5>}
    pass
class Domain():
    """
    Members:

      MD

      TVD

      TVDSS

      TVDSD

      TWT

      OWT
    """
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __gt__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    MD: h5geopy._h5geo.Domain # value = <Domain.MD: 1>
    OWT: h5geopy._h5geo.Domain # value = <Domain.OWT: 32>
    TVD: h5geopy._h5geo.Domain # value = <Domain.TVD: 2>
    TVDSD: h5geopy._h5geo.Domain # value = <Domain.TVDSD: 8>
    TVDSS: h5geopy._h5geo.Domain # value = <Domain.TVDSS: 4>
    TWT: h5geopy._h5geo.Domain # value = <Domain.TWT: 16>
    __members__: dict # value = {'MD': <Domain.MD: 1>, 'TVD': <Domain.TVD: 2>, 'TVDSS': <Domain.TVDSS: 4>, 'TVDSD': <Domain.TVDSD: 8>, 'TWT': <Domain.TWT: 16>, 'OWT': <Domain.OWT: 32>}
    pass
class _H5Base():
    pass
class H5Base(_H5Base):
    def Delete(self) -> None: ...
    def getChildList(self, arg0: h5gtpy._h5gt.Group, arg1: ObjectType) -> typing.List[h5gtpy._h5gt.Group]: ...
    pass
class _H5BaseObject(_H5Base):
    pass
class H5BaseObject(H5Base, _H5BaseObject, _H5Base):
    def getDatasetOpt(self, arg0: h5gtpy._h5gt.Group, arg1: str) -> typing.Optional[h5gtpy._h5gt.DataSet]: ...
    def getFullName(self) -> str: ...
    def getGroupOpt(self, arg0: h5gtpy._h5gt.Group, arg1: str) -> typing.Optional[h5gtpy._h5gt.Group]: ...
    def getH5File(self) -> h5gtpy._h5gt.File: ...
    def getName(self) -> str: ...
    def getObjG(self) -> h5gtpy._h5gt.Group: ...
    pass
class _H5LogCurve(_H5BaseObject, _H5Base):
    pass
class _H5Seis(_H5BaseObject, _H5Base):
    pass
class _H5BaseContainer(_H5Base):
    pass
class _H5Surf(_H5BaseObject, _H5Base):
    pass
class H5BaseContainer(H5Base, _H5BaseContainer, _H5Base):
    def getH5File(self) -> h5gtpy._h5gt.File: ...
    pass
class _H5Well(_H5BaseObject, _H5Base):
    pass
class _H5WellContainer(_H5BaseContainer, _H5Base):
    pass
class LogCurveParam():
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, spatialUnits: SpatialUnits, dataUnits: str, chunkSize: int = 1000) -> None: ...
    @property
    def chunkSize(self) -> int:
        """
        :type: int
        """
    @chunkSize.setter
    def chunkSize(self, arg0: int) -> None:
        pass
    @property
    def dataUnits(self) -> str:
        """
        :type: str
        """
    @dataUnits.setter
    def dataUnits(self, arg0: str) -> None:
        pass
    @property
    def spatialUnits(self) -> SpatialUnits:
        """
        :type: SpatialUnits
        """
    @spatialUnits.setter
    def spatialUnits(self, arg0: SpatialUnits) -> None:
        pass
    pass
class LogDataType():
    """
    Members:

      MD

      VAL
    """
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __gt__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    MD: h5geopy._h5geo.LogDataType # value = <LogDataType.MD: 1>
    VAL: h5geopy._h5geo.LogDataType # value = <LogDataType.VAL: 2>
    __members__: dict # value = {'MD': <LogDataType.MD: 1>, 'VAL': <LogDataType.VAL: 2>}
    pass
class ObjectType():
    """
    Members:

      SURFACE

      WELL

      LOGCURVE

      DEVCURVE

      SEISMIC
    """
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __gt__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    DEVCURVE: h5geopy._h5geo.ObjectType # value = <ObjectType.DEVCURVE: 4>
    LOGCURVE: h5geopy._h5geo.ObjectType # value = <ObjectType.LOGCURVE: 3>
    SEISMIC: h5geopy._h5geo.ObjectType # value = <ObjectType.SEISMIC: 5>
    SURFACE: h5geopy._h5geo.ObjectType # value = <ObjectType.SURFACE: 1>
    WELL: h5geopy._h5geo.ObjectType # value = <ObjectType.WELL: 2>
    __members__: dict # value = {'SURFACE': <ObjectType.SURFACE: 1>, 'WELL': <ObjectType.WELL: 2>, 'LOGCURVE': <ObjectType.LOGCURVE: 3>, 'DEVCURVE': <ObjectType.DEVCURVE: 4>, 'SEISMIC': <ObjectType.SEISMIC: 5>}
    pass
class SegyEndian():
    """
    Members:

      Little

      Big
    """
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __gt__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    Big: h5geopy._h5geo.SegyEndian # value = <SegyEndian.Big: 1>
    Little: h5geopy._h5geo.SegyEndian # value = <SegyEndian.Little: 0>
    __members__: dict # value = {'Little': <SegyEndian.Little: 0>, 'Big': <SegyEndian.Big: 1>}
    pass
class SegyFormat():
    """
    Members:

      FourByte_IBM

      FourByte_IEEE

      FourByte_integer
    """
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __gt__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    FourByte_IBM: h5geopy._h5geo.SegyFormat # value = <SegyFormat.FourByte_IBM: 0>
    FourByte_IEEE: h5geopy._h5geo.SegyFormat # value = <SegyFormat.FourByte_IEEE: 1>
    FourByte_integer: h5geopy._h5geo.SegyFormat # value = <SegyFormat.FourByte_integer: 2>
    __members__: dict # value = {'FourByte_IBM': <SegyFormat.FourByte_IBM: 0>, 'FourByte_IEEE': <SegyFormat.FourByte_IEEE: 1>, 'FourByte_integer': <SegyFormat.FourByte_integer: 2>}
    pass
class SeisDataType():
    """
    Members:

      STACK

      PRESTACK

      ATTRIBUTE
    """
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __gt__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    ATTRIBUTE: h5geopy._h5geo.SeisDataType # value = <SeisDataType.ATTRIBUTE: 3>
    PRESTACK: h5geopy._h5geo.SeisDataType # value = <SeisDataType.PRESTACK: 2>
    STACK: h5geopy._h5geo.SeisDataType # value = <SeisDataType.STACK: 1>
    __members__: dict # value = {'STACK': <SeisDataType.STACK: 1>, 'PRESTACK': <SeisDataType.PRESTACK: 2>, 'ATTRIBUTE': <SeisDataType.ATTRIBUTE: 3>}
    pass
class SeisParam():
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, domain: Domain, spatialUnits: SpatialUnits, temporalUnits: TemporalUnits, dataUnits: str, dataType: SeisDataType, surveyType: SurveyType, nTrc: int, nSamp: int, srd: float = 0, trcChunk: int = 20000, stdChunk: int = 1000) -> None: ...
    @property
    def dataType(self) -> SeisDataType:
        """
        :type: SeisDataType
        """
    @dataType.setter
    def dataType(self, arg0: SeisDataType) -> None:
        pass
    @property
    def dataUnits(self) -> str:
        """
        :type: str
        """
    @dataUnits.setter
    def dataUnits(self, arg0: str) -> None:
        pass
    @property
    def domain(self) -> Domain:
        """
        :type: Domain
        """
    @domain.setter
    def domain(self, arg0: Domain) -> None:
        pass
    @property
    def nSamp(self) -> int:
        """
        :type: int
        """
    @nSamp.setter
    def nSamp(self, arg0: int) -> None:
        pass
    @property
    def nTrc(self) -> int:
        """
        :type: int
        """
    @nTrc.setter
    def nTrc(self, arg0: int) -> None:
        pass
    @property
    def spatialUnits(self) -> SpatialUnits:
        """
        :type: SpatialUnits
        """
    @spatialUnits.setter
    def spatialUnits(self, arg0: SpatialUnits) -> None:
        pass
    @property
    def srd(self) -> float:
        """
        :type: float
        """
    @srd.setter
    def srd(self, arg0: float) -> None:
        pass
    @property
    def stdChunk(self) -> int:
        """
        :type: int
        """
    @stdChunk.setter
    def stdChunk(self, arg0: int) -> None:
        pass
    @property
    def surveyType(self) -> SurveyType:
        """
        :type: SurveyType
        """
    @surveyType.setter
    def surveyType(self, arg0: SurveyType) -> None:
        pass
    @property
    def temporalUnits(self) -> TemporalUnits:
        """
        :type: TemporalUnits
        """
    @temporalUnits.setter
    def temporalUnits(self, arg0: TemporalUnits) -> None:
        pass
    @property
    def trcChunk(self) -> int:
        """
        :type: int
        """
    @trcChunk.setter
    def trcChunk(self, arg0: int) -> None:
        pass
    pass
class SpatialUnits():
    """
    Members:

      METER

      CENTIMETER

      MILLIMETER

      FOOT
    """
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __gt__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    CENTIMETER: h5geopy._h5geo.SpatialUnits # value = <SpatialUnits.CENTIMETER: 1>
    FOOT: h5geopy._h5geo.SpatialUnits # value = <SpatialUnits.FOOT: 3>
    METER: h5geopy._h5geo.SpatialUnits # value = <SpatialUnits.METER: 0>
    MILLIMETER: h5geopy._h5geo.SpatialUnits # value = <SpatialUnits.MILLIMETER: 2>
    __members__: dict # value = {'METER': <SpatialUnits.METER: 0>, 'CENTIMETER': <SpatialUnits.CENTIMETER: 1>, 'MILLIMETER': <SpatialUnits.MILLIMETER: 2>, 'FOOT': <SpatialUnits.FOOT: 3>}
    pass
class SurfParam():
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, nX: int, nY: int, X0: float, Y0: float, dX: float, dY: float, domain: Domain, spatialUnits: SpatialUnits, temporalUnits: TemporalUnits, dataUnits: str) -> None: ...
    @property
    def X0(self) -> float:
        """
        :type: float
        """
    @X0.setter
    def X0(self, arg0: float) -> None:
        pass
    @property
    def Y0(self) -> float:
        """
        :type: float
        """
    @Y0.setter
    def Y0(self, arg0: float) -> None:
        pass
    @property
    def dX(self) -> float:
        """
        :type: float
        """
    @dX.setter
    def dX(self, arg0: float) -> None:
        pass
    @property
    def dY(self) -> float:
        """
        :type: float
        """
    @dY.setter
    def dY(self, arg0: float) -> None:
        pass
    @property
    def dataUnits(self) -> str:
        """
        :type: str
        """
    @dataUnits.setter
    def dataUnits(self, arg0: str) -> None:
        pass
    @property
    def domain(self) -> Domain:
        """
        :type: Domain
        """
    @domain.setter
    def domain(self, arg0: Domain) -> None:
        pass
    @property
    def nX(self) -> int:
        """
        :type: int
        """
    @nX.setter
    def nX(self, arg0: int) -> None:
        pass
    @property
    def nY(self) -> int:
        """
        :type: int
        """
    @nY.setter
    def nY(self, arg0: int) -> None:
        pass
    @property
    def spatialUnits(self) -> SpatialUnits:
        """
        :type: SpatialUnits
        """
    @spatialUnits.setter
    def spatialUnits(self, arg0: SpatialUnits) -> None:
        pass
    @property
    def temporalUnits(self) -> TemporalUnits:
        """
        :type: TemporalUnits
        """
    @temporalUnits.setter
    def temporalUnits(self, arg0: TemporalUnits) -> None:
        pass
    pass
class SurveyType():
    """
    Members:

      TWO_D

      THREE_D
    """
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __gt__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    THREE_D: h5geopy._h5geo.SurveyType # value = <SurveyType.THREE_D: 2>
    TWO_D: h5geopy._h5geo.SurveyType # value = <SurveyType.TWO_D: 1>
    __members__: dict # value = {'TWO_D': <SurveyType.TWO_D: 1>, 'THREE_D': <SurveyType.THREE_D: 2>}
    pass
class TemporalUnits():
    """
    Members:

      SECOND

      MILLISECOND

      MICROSECOND
    """
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __gt__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    MICROSECOND: h5geopy._h5geo.TemporalUnits # value = <TemporalUnits.MICROSECOND: 2>
    MILLISECOND: h5geopy._h5geo.TemporalUnits # value = <TemporalUnits.MILLISECOND: 1>
    SECOND: h5geopy._h5geo.TemporalUnits # value = <TemporalUnits.SECOND: 0>
    __members__: dict # value = {'SECOND': <TemporalUnits.SECOND: 0>, 'MILLISECOND': <TemporalUnits.MILLISECOND: 1>, 'MICROSECOND': <TemporalUnits.MICROSECOND: 2>}
    pass
class TrajectoryFormat():
    """
    Members:

      MD_AZIM_INCL

      TVD_X_Y

      TVD_DX_DY

      TVDSS_X_Y

      TVDSS_DX_DY
    """
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __gt__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    MD_AZIM_INCL: h5geopy._h5geo.TrajectoryFormat # value = <TrajectoryFormat.MD_AZIM_INCL: 0>
    TVDSS_DX_DY: h5geopy._h5geo.TrajectoryFormat # value = <TrajectoryFormat.TVDSS_DX_DY: 4>
    TVDSS_X_Y: h5geopy._h5geo.TrajectoryFormat # value = <TrajectoryFormat.TVDSS_X_Y: 3>
    TVD_DX_DY: h5geopy._h5geo.TrajectoryFormat # value = <TrajectoryFormat.TVD_DX_DY: 2>
    TVD_X_Y: h5geopy._h5geo.TrajectoryFormat # value = <TrajectoryFormat.TVD_X_Y: 1>
    __members__: dict # value = {'MD_AZIM_INCL': <TrajectoryFormat.MD_AZIM_INCL: 0>, 'TVD_X_Y': <TrajectoryFormat.TVD_X_Y: 1>, 'TVD_DX_DY': <TrajectoryFormat.TVD_DX_DY: 2>, 'TVDSS_X_Y': <TrajectoryFormat.TVDSS_X_Y: 3>, 'TVDSS_DX_DY': <TrajectoryFormat.TVDSS_DX_DY: 4>}
    pass
class TxtEncoding():
    """
    Members:

      ASCII

      EBCDIC
    """
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __gt__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    ASCII: h5geopy._h5geo.TxtEncoding # value = <TxtEncoding.ASCII: 0>
    EBCDIC: h5geopy._h5geo.TxtEncoding # value = <TxtEncoding.EBCDIC: 1>
    __members__: dict # value = {'ASCII': <TxtEncoding.ASCII: 0>, 'EBCDIC': <TxtEncoding.EBCDIC: 1>}
    pass
class WellDataType():
    """
    Members:

      WELL

      DEV

      LOG

      INTERVAL_VEL

      AVG_VEL

      RMS_VEL

      FWAL

      CHECKSHOTS

      WELL_TIE
    """
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __gt__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    AVG_VEL: h5geopy._h5geo.WellDataType # value = <WellDataType.AVG_VEL: 5>
    CHECKSHOTS: h5geopy._h5geo.WellDataType # value = <WellDataType.CHECKSHOTS: 8>
    DEV: h5geopy._h5geo.WellDataType # value = <WellDataType.DEV: 2>
    FWAL: h5geopy._h5geo.WellDataType # value = <WellDataType.FWAL: 7>
    INTERVAL_VEL: h5geopy._h5geo.WellDataType # value = <WellDataType.INTERVAL_VEL: 4>
    LOG: h5geopy._h5geo.WellDataType # value = <WellDataType.LOG: 3>
    RMS_VEL: h5geopy._h5geo.WellDataType # value = <WellDataType.RMS_VEL: 6>
    WELL: h5geopy._h5geo.WellDataType # value = <WellDataType.WELL: 1>
    WELL_TIE: h5geopy._h5geo.WellDataType # value = <WellDataType.WELL_TIE: 9>
    __members__: dict # value = {'WELL': <WellDataType.WELL: 1>, 'DEV': <WellDataType.DEV: 2>, 'LOG': <WellDataType.LOG: 3>, 'INTERVAL_VEL': <WellDataType.INTERVAL_VEL: 4>, 'AVG_VEL': <WellDataType.AVG_VEL: 5>, 'RMS_VEL': <WellDataType.RMS_VEL: 6>, 'FWAL': <WellDataType.FWAL: 7>, 'CHECKSHOTS': <WellDataType.CHECKSHOTS: 8>, 'WELL_TIE': <WellDataType.WELL_TIE: 9>}
    pass
class WellName():
    """
    Members:

      FROM_LAS

      FROM_FILE_NAME
    """
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __gt__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    FROM_FILE_NAME: h5geopy._h5geo.WellName # value = <WellName.FROM_FILE_NAME: 1>
    FROM_LAS: h5geopy._h5geo.WellName # value = <WellName.FROM_LAS: 0>
    __members__: dict # value = {'FROM_LAS': <WellName.FROM_LAS: 0>, 'FROM_FILE_NAME': <WellName.FROM_FILE_NAME: 1>}
    pass
class WellParam():
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, headX: float, headY: float, kb: float, uwi: str, spatialUnits: SpatialUnits) -> None: ...
    @property
    def headX(self) -> float:
        """
        :type: float
        """
    @headX.setter
    def headX(self, arg0: float) -> None:
        pass
    @property
    def headY(self) -> float:
        """
        :type: float
        """
    @headY.setter
    def headY(self, arg0: float) -> None:
        pass
    @property
    def kb(self) -> float:
        """
        :type: float
        """
    @kb.setter
    def kb(self, arg0: float) -> None:
        pass
    @property
    def spatialUnits(self) -> SpatialUnits:
        """
        :type: SpatialUnits
        """
    @spatialUnits.setter
    def spatialUnits(self, arg0: SpatialUnits) -> None:
        pass
    @property
    def uwi(self) -> str:
        """
        :type: str
        """
    @uwi.setter
    def uwi(self, arg0: str) -> None:
        pass
    pass
class WellType():
    """
    Members:

      PROPOSED

      DRY

      OIL

      GAS

      WATER

      CONDENSATE
    """
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __gt__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    CONDENSATE: h5geopy._h5geo.WellType # value = <WellType.CONDENSATE: 32>
    DRY: h5geopy._h5geo.WellType # value = <WellType.DRY: 2>
    GAS: h5geopy._h5geo.WellType # value = <WellType.GAS: 8>
    OIL: h5geopy._h5geo.WellType # value = <WellType.OIL: 4>
    PROPOSED: h5geopy._h5geo.WellType # value = <WellType.PROPOSED: 1>
    WATER: h5geopy._h5geo.WellType # value = <WellType.WATER: 16>
    __members__: dict # value = {'PROPOSED': <WellType.PROPOSED: 1>, 'DRY': <WellType.DRY: 2>, 'OIL': <WellType.OIL: 4>, 'GAS': <WellType.GAS: 8>, 'WATER': <WellType.WATER: 16>, 'CONDENSATE': <WellType.CONDENSATE: 32>}
    pass
class _H5SeisContainer(_H5BaseContainer, _H5Base):
    pass
class _H5SurfContainer(_H5BaseContainer, _H5Base):
    pass
class _H5DevCurve(_H5BaseObject, _H5Base):
    pass
class H5DevCurve(H5BaseObject, H5Base, _H5DevCurve, _H5BaseObject, _H5Base):
    @typing.overload
    def getCurve(self, arg0: DevDataType) -> numpy.ndarray[numpy.float64, _Shape[m, 1]]: ...
    @typing.overload
    def getCurve(self, arg0: str) -> numpy.ndarray[numpy.float64, _Shape[m, 1]]: ...
    def getDevCurveD(self) -> typing.Optional[h5gtpy._h5gt.DataSet]: ...
    def getNCurves(self) -> int: ...
    def getNSamp(self) -> int: ...
    def getRelativeCurveName(self) -> str: ...
    def getWell(self) -> _H5Well: ...
    def getWellContainer(self) -> _H5WellContainer: ...
    def isActive(self) -> bool: ...
    def setActive(self) -> bool: ...
    @typing.overload
    def writeCurve(self, arg0: DevDataType, arg1: numpy.ndarray[numpy.float64, _Shape[m, 1]]) -> bool: ...
    @typing.overload
    def writeCurve(self, arg0: str, arg1: numpy.ndarray[numpy.float64, _Shape[m, 1]]) -> bool: ...
    pass
class H5LogCurve(H5BaseObject, H5Base, _H5LogCurve, _H5BaseObject, _H5Base):
    @typing.overload
    def getCurve(self, arg0: LogDataType) -> numpy.ndarray[numpy.float64, _Shape[m, 1]]: ...
    @typing.overload
    def getCurve(self, arg0: str) -> numpy.ndarray[numpy.float64, _Shape[m, 1]]: ...
    def getLogCurveD(self) -> typing.Optional[h5gtpy._h5gt.DataSet]: ...
    def getRelativeCurveName(self) -> str: ...
    def getWell(self) -> _H5Well: ...
    def getWellContainer(self) -> _H5WellContainer: ...
    @typing.overload
    def writeCurve(self, arg0: LogDataType, arg1: numpy.ndarray[numpy.float64, _Shape[m, 1]]) -> bool: ...
    @typing.overload
    def writeCurve(self, arg0: str, arg1: numpy.ndarray[numpy.float64, _Shape[m, 1]]) -> bool: ...
    pass
class H5Seis(H5BaseObject, H5Base, _H5Seis, _H5BaseObject, _H5Base):
    def addPKeySort(self, pKeyName: str) -> bool: ...
    def calcAndWriteBoundary(self) -> bool: 
        """
        calculate boundary for any seismic survey type and write it. Retun true if successful
        """
    def calcAndWriteTraceHeaderLimits(self, nTrcBuffer: int = 1e7) -> bool: 
        """
        calculate and write min and max values for each header. By default trace buffer is set `nTrcBuffer` to 10 millions of traces

        calculate and write min and max values for each header. This is needed by some operations. By default trace buffer is set `nTrcBuffer` to 10 millions of traces
        """
    def calcBinOriginOrientation3DStk(self) -> typing.Tuple[numpy.ndarray[numpy.float64, _Shape[2, 1]], numpy.ndarray[numpy.float64, _Shape[2, 1]], float, bool]: 
        """
        calculate `bin` (along `INLINE` and `XLINE` respectively)`, `origin` (`XY` point coordinate where sorted: 1) INLINE->min, 2) CDP_X->min, 3) CDP_Y->min),`orientation` an azimuth along `INLINE` (in radians). All these parameters are needed when displaying in VTK scene.Also returns `bool val` set to true if successful.
        """
    def calcBoundaryStk2D(self) -> numpy.ndarray[numpy.float64, _Shape[m, 2]]: 
        """
        calculate boundary for 2D stk seismic
        """
    def calcConvexHullBoundary(self) -> numpy.ndarray[numpy.float64, _Shape[m, 2]]: 
        """
        calculate convex boundary (usually used in 3D seismic or 2D prestack seismic)
        """
    def checkSampleLimits(self, fromSampInd: int, nSamp: int) -> typing.Tuple[int, bool]: 
        """
        check 'fromSampInd' and 'nSamp' and diminish 'nSamp' to fit in data limits (if 'fromSampInd' is inside limit)`fromSampInd` first index (the value should be less then number of samples)`nSamp` number of samples (to read for example). Return corrected `nSamp`
        """
    def checkTraceHeaderLimits(self, fromHdr: int, nHdr: int) -> typing.Tuple[int, bool]: 
        """
        check 'fromHdr' and 'nHdr' and diminish 'nHdr' to fit in data limits (if 'fromHdr' is inside limit)`fromHdr` first header (usually there are 78 headers so the value should be less then this value)`nHdr` number of headers (to read for example). Return corrected `nHdr`
        """
    def checkTraceLimits(self, fromTrc: int, nTrc: int) -> typing.Tuple[int, bool]: 
        """
        check 'fromTrc' and 'nTrc' and diminish 'nTrc' to fit in data limits (if 'fromTrc' is inside limit)`fromTrc` first trace (the value should be less then number of traces)`nTrc` number of traces (to read for example). Return corrected `nTrc`
        """
    @typing.overload
    def getBinHeader(self) -> numpy.ndarray[numpy.float64, _Shape[m, 1]]: ...
    @typing.overload
    def getBinHeader(self, hdrName: str) -> float: ...
    def getBinHeaderD(self) -> typing.Optional[h5gtpy._h5gt.DataSet]: ...
    def getBinHeaderIndex(self, hdrName: str) -> int: ...
    def getBoundaryD(self) -> typing.Optional[h5gtpy._h5gt.DataSet]: ...
    def getDataType(self) -> SeisDataType: ...
    def getFirstSample(self, trcInd: int) -> float: 
        """
        in units according to `Domain` (`METER` or `SECOND` or else...)
        """
    def getIndexesG(self) -> typing.Optional[h5gtpy._h5gt.Group]: ...
    def getLastSample(self, trcInd: int) -> float: 
        """
        in units according to `Domain` (`METER` or `SECOND` or else...)
        """
    def getNBinHdr(self) -> int: 
        """
        get number of bin headers
        """
    def getNSamp(self) -> int: 
        """
        get number of samples (i.e. trace length)
        """
    def getNTextHdrRows(self) -> int: 
        """
        get number lines of text header
        """
    def getNTrc(self) -> int: 
        """
        get number of traces
        """
    def getNTrcHdr(self) -> int: 
        """
        get number of trace headers (usually 78)
        """
    def getPKeyNames(self) -> typing.List[str]: 
        """
        get primary key names (usually they are used in sorting)
        """
    def getSampRate(self) -> float: 
        """
        in units according to `Domain` (`METER` or `SECOND` or else...)
        """
    def getSamples(self, trcInd: int) -> numpy.ndarray[numpy.float64, _Shape[m, 1]]: 
        """
        in units according to `Domain` (`METER` or `SECOND` or else...)
        """
    def getSeisContainer(self) -> _H5SeisContainer: ...
    def getSortG(self) -> typing.Optional[h5gtpy._h5gt.Group]: ...
    def getSortedData(self, keyList: typing.List[str], minList: typing.List[float], maxList: typing.List[float], fromSampInd: int = 0, nSamp: int = sys.maxint) -> typing.Tuple[numpy.ndarray[numpy.float32, _Shape[m, n]], numpy.ndarray[numpy.float64, _Shape[m, n]], numpy.ndarray[numpy.uint64, _Shape[m, 1]]]: 
        """
        Get sorted data based on precalculated primary sort keys (e.g. before using it you should prepare primary sort keys with `addPKeySort(...)` method).Return `TRACE` (traces matrix), `HDR` (hdr matrix) and `idx` (vector of trace indexes read)
        """
    def getSurveyType(self) -> SurveyType: ...
    def getTextHeader(self) -> typing.List[str]: ...
    def getTextHeaderD(self) -> typing.Optional[h5gtpy._h5gt.DataSet]: ...
    def getTrace(self, fromTrc: int, nTrc: int = 1, fromSampInd: int = 0, nSamp: int = sys.maxint) -> numpy.ndarray[numpy.float32, _Shape[m, n]]: 
        """
        Get block of traces. If `nTrc` or `nSamp` exceed max values then these values are changed to max allowed (that is why they are not `const`)
        """
    def getTraceD(self) -> typing.Optional[h5gtpy._h5gt.DataSet]: ...
    @typing.overload
    def getTraceHeader(self, fromTrc: int, nTrc: int = 1, fromHdr: int = 0, nHdr: int = sys.maxint) -> numpy.ndarray[numpy.float64, _Shape[m, n]]: 
        """
        Get block of trace headers. If `nTrc` or `nHdr` exceed max values then these values are changed to max allowed (that is why they are not `const`)
        """
    @typing.overload
    def getTraceHeader(self, hdrName: str, fromTrc: int = 0, nTrc: int = sys.maxint) -> numpy.ndarray[numpy.float64, _Shape[m, 1]]: ...
    def getTraceHeaderD(self) -> typing.Optional[h5gtpy._h5gt.DataSet]: ...
    def getTraceHeaderIndex(self, hdrName: str) -> int: ...
    @typing.overload
    def getTraceHeaderMax(self) -> numpy.ndarray[numpy.float64, _Shape[m, 1]]: ...
    @typing.overload
    def getTraceHeaderMax(self, hdrName: str) -> float: ...
    @typing.overload
    def getTraceHeaderMin(self) -> numpy.ndarray[numpy.float64, _Shape[m, 1]]: ...
    @typing.overload
    def getTraceHeaderMin(self, hdrName: str) -> float: ...
    def getTracePKeyIndexes(self, pName: str, pMin: float, pMax: float) -> numpy.ndarray[numpy.uint64, _Shape[m, 1]]: ...
    def getUValG(self) -> typing.Optional[h5gtpy._h5gt.Group]: ...
    def hasPKeySort(self, pKeyName: str) -> bool: ...
    def removePKeySort(self, pKeyName: str) -> bool: ...
    @typing.overload
    def writeBinHeader(self, binHdr: numpy.ndarray[numpy.float64, _Shape[m, 1]]) -> bool: ...
    @typing.overload
    def writeBinHeader(self, binHdr: typing.List[float]) -> bool: ...
    @typing.overload
    def writeBinHeader(self, hdrName: str, value: float) -> bool: ...
    def writeBoundary(self, boundary: numpy.ndarray[numpy.float64, _Shape[m, 2]]) -> bool: 
        """
        write boundary of 2d (a line) or 3d (usually convex hull or concave hull) seismic survey. Input argument is `MatrixX2d` where first col - `X` coord, second - `Y` coord
        """
    def writeTextHeader(self, txtHdr: typing.List[str]) -> bool: ...
    def writeTrace(self, arg0: numpy.ndarray[numpy.float32, _Shape[m, n]], arg1: int, arg2: int) -> bool: ...
    @typing.overload
    def writeTraceHeader(self, HDR: numpy.ndarray[numpy.float64, _Shape[m, n]], fromTrc: int = 0, fromHdrInd: int = 0) -> bool: ...
    @typing.overload
    def writeTraceHeader(self, hdrName: str, hdr: numpy.ndarray[numpy.float64, _Shape[m, n]], fromTrc: int = 0) -> bool: ...
    pass
class H5SeisContainer(H5BaseContainer, H5Base, _H5SeisContainer, _H5BaseContainer, _H5Base):
    @typing.overload
    def createSeis(self, arg0: h5gtpy._h5gt.Group, arg1: SeisParam, arg2: CreationType) -> _H5Seis: ...
    @typing.overload
    def createSeis(self, arg0: str, arg1: SeisParam, arg2: CreationType) -> _H5Seis: ...
    @typing.overload
    def getSeis(self, arg0: h5gtpy._h5gt.Group) -> _H5Seis: ...
    @typing.overload
    def getSeis(self, arg0: str) -> _H5Seis: ...
    def getSeisList(self) -> typing.List[_H5Seis]: ...
    pass
class H5Surf(H5BaseObject, H5Base, _H5Surf, _H5BaseObject, _H5Base):
    def getData(self) -> numpy.ndarray[numpy.float64, _Shape[m, n]]: ...
    def getSurfContainer(self) -> _H5SurfContainer: ...
    def getSurfD(self) -> typing.Optional[h5gtpy._h5gt.DataSet]: ...
    def writeData(self, arg0: numpy.ndarray[numpy.float64, _Shape[m, n]]) -> bool: ...
    pass
class H5SurfContainer(H5BaseContainer, H5Base, _H5SurfContainer, _H5BaseContainer, _H5Base):
    @typing.overload
    def createSurf(self, arg0: h5gtpy._h5gt.Group, arg1: SurfParam, arg2: CreationType) -> _H5Surf: ...
    @typing.overload
    def createSurf(self, arg0: str, arg1: SurfParam, arg2: CreationType) -> _H5Surf: ...
    @typing.overload
    def getSurf(self, arg0: h5gtpy._h5gt.Group) -> _H5Surf: ...
    @typing.overload
    def getSurf(self, arg0: str) -> _H5Surf: ...
    def getSurfList(self) -> typing.List[_H5Surf]: ...
    pass
class H5Well(H5BaseObject, H5Base, _H5Well, _H5BaseObject, _H5Base):
    @typing.overload
    def createDevCurve(self, arg0: h5gtpy._h5gt.Group, arg1: DevCurveParam, arg2: CreationType) -> _H5DevCurve: ...
    @typing.overload
    def createDevCurve(self, arg0: str, arg1: DevCurveParam, arg2: CreationType) -> _H5DevCurve: ...
    @typing.overload
    def createLogCurve(self, arg0: h5gtpy._h5gt.Group, arg1: LogCurveParam, arg2: CreationType) -> _H5LogCurve: ...
    @typing.overload
    def createLogCurve(self, arg0: str, arg1: str, arg2: LogCurveParam, arg3: CreationType) -> _H5LogCurve: ...
    def getActiveDevCurve(self) -> _H5DevCurve: ...
    def getActiveDevG(self) -> typing.Optional[h5gtpy._h5gt.Group]: ...
    @typing.overload
    def getDevCurve(self, arg0: h5gtpy._h5gt.Group) -> _H5DevCurve: ...
    @typing.overload
    def getDevCurve(self, arg0: str) -> _H5DevCurve: ...
    def getDevCurveList(self) -> typing.List[_H5DevCurve]: ...
    def getDevCurveNameList(self) -> typing.List[str]: ...
    def getDevG(self) -> typing.Optional[h5gtpy._h5gt.Group]: ...
    def getHeadCoord(self) -> numpy.ndarray[numpy.float64, _Shape[2, 1]]: ...
    def getKB(self) -> float: ...
    @typing.overload
    def getLogCurve(self, arg0: h5gtpy._h5gt.Group) -> _H5LogCurve: ...
    @typing.overload
    def getLogCurve(self, arg0: str, arg1: str) -> _H5LogCurve: ...
    def getLogCurveList(self) -> typing.List[_H5LogCurve]: ...
    def getLogCurveNameList(self) -> typing.List[str]: ...
    def getLogG(self) -> typing.Optional[h5gtpy._h5gt.Group]: ...
    def getLogTypeG(self, arg0: str) -> typing.Optional[h5gtpy._h5gt.Group]: ...
    def getLogTypeNameList(self) -> typing.List[str]: ...
    def getUWI(self) -> str: ...
    def getWellContainer(self) -> _H5WellContainer: ...
    def setHeadCoord(self, arg0: numpy.ndarray[numpy.float64, _Shape[2, 1]]) -> bool: ...
    def setKB(self, arg0: float) -> bool: ...
    def setUWI(self, arg0: str) -> bool: ...
    pass
class H5WellContainer(H5BaseContainer, H5Base, _H5WellContainer, _H5BaseContainer, _H5Base):
    @typing.overload
    def createWell(self, arg0: h5gtpy._h5gt.Group, arg1: WellParam, arg2: CreationType) -> _H5Well: ...
    @typing.overload
    def createWell(self, arg0: str, arg1: WellParam, arg2: CreationType) -> _H5Well: ...
    @typing.overload
    def getWell(self, arg0: h5gtpy._h5gt.Group) -> _H5Well: ...
    @typing.overload
    def getWell(self, arg0: str) -> _H5Well: ...
    def getWellList(self) -> typing.List[_H5Well]: ...
    pass
@typing.overload
def MdAzIncl2ALL(M: numpy.ndarray[numpy.float32, _Shape[m, n]], x0: float, y0: float, kb: float, angleUnits: AngleUnits, XNorth: bool) -> numpy.ndarray[numpy.float32, _Shape[m, n]]:
    """
    Convert matrix `M` (whose columns represent MD Az Incl respectively)to `MD_X_Y_Z_TVD_DX_DY_AZ_INCL` (Z the same as TVDSS). Set `XNorth` to `True` if `X` axis points to the North
    """
@typing.overload
def MdAzIncl2ALL(M: numpy.ndarray[numpy.float64, _Shape[m, n]], x0: float, y0: float, kb: float, angleUnits: AngleUnits, XNorth: bool) -> numpy.ndarray[numpy.float64, _Shape[m, n]]:
    pass
@typing.overload
def MdAzIncl2MdXYTvd(M: numpy.ndarray[numpy.float32, _Shape[m, n]], x0: float, y0: float, angleUnits: AngleUnits, XNorth: bool) -> numpy.ndarray[numpy.float32, _Shape[m, n]]:
    """
    Convert matrix `M` (whose columns represent MD Az Incl respectively)to `MD_X_Y_TVD`. Set `XNorth` to `True` if `X` axis points to the North
    """
@typing.overload
def MdAzIncl2MdXYTvd(M: numpy.ndarray[numpy.float64, _Shape[m, n]], x0: float, y0: float, angleUnits: AngleUnits, XNorth: bool) -> numpy.ndarray[numpy.float64, _Shape[m, n]]:
    pass
@typing.overload
def TvdDxDy2ALL(M: numpy.ndarray[numpy.float32, _Shape[m, n]], x0: float, y0: float, kb: float, XNorth: bool) -> numpy.ndarray[numpy.float32, _Shape[m, n]]:
    """
    Convert matrix `M` (whose columns represent TVD DX DY respectively)to `MD_X_Y_Z_TVD_DX_DY_AZ_INCL` (Z the same as TVDSS). Set `XNorth` to `True` if `X` axis points to the North
    """
@typing.overload
def TvdDxDy2ALL(M: numpy.ndarray[numpy.float64, _Shape[m, n]], x0: float, y0: float, kb: float, XNorth: bool) -> numpy.ndarray[numpy.float64, _Shape[m, n]]:
    pass
@typing.overload
def TvdDxDy2MdAzIncl(M: numpy.ndarray[numpy.float32, _Shape[m, n]], XNorth: bool) -> numpy.ndarray[numpy.float32, _Shape[m, n]]:
    """
    Convert matrix `M` (whose columns represent TVD DX DY respectively)to `MD_Az_Incl`. Set `XNorth` to `True` if `X` axis points to the North
    """
@typing.overload
def TvdDxDy2MdAzIncl(M: numpy.ndarray[numpy.float64, _Shape[m, n]], XNorth: bool) -> numpy.ndarray[numpy.float64, _Shape[m, n]]:
    pass
@typing.overload
def TvdDxDy2MdXYTvd(M: numpy.ndarray[numpy.float32, _Shape[m, n]], x0: float, y0: float, XNorth: bool) -> numpy.ndarray[numpy.float32, _Shape[m, n]]:
    """
    Convert matrix `M` (whose columns represent TVD DX DY respectively)to `MD_X_Y_TVD`. Set `XNorth` to `True` if `X` axis points to the North
    """
@typing.overload
def TvdDxDy2MdXYTvd(M: numpy.ndarray[numpy.float64, _Shape[m, n]], x0: float, y0: float, XNorth: bool) -> numpy.ndarray[numpy.float64, _Shape[m, n]]:
    pass
@typing.overload
def TvdXY2ALL(M: numpy.ndarray[numpy.float32, _Shape[m, n]], x0: float, y0: float, kb: float, XNorth: bool) -> numpy.ndarray[numpy.float32, _Shape[m, n]]:
    """
    Convert matrix `M` (whose columns represent TVD X Y respectively)to `MD_X_Y_Z_TVD_DX_DY_AZ_INCL` (Z the same as TVDSS). Set `XNorth` to `True` if `X` axis points to the North
    """
@typing.overload
def TvdXY2ALL(M: numpy.ndarray[numpy.float64, _Shape[m, n]], x0: float, y0: float, kb: float, XNorth: bool) -> numpy.ndarray[numpy.float64, _Shape[m, n]]:
    pass
@typing.overload
def TvdXY2MdAzIncl(M: numpy.ndarray[numpy.float32, _Shape[m, n]], x0: float, y0: float, XNorth: bool) -> numpy.ndarray[numpy.float32, _Shape[m, n]]:
    """
    Convert matrix `M` (whose columns represent TVD X Y respectively)to `MD_Az_Incl`. Set `XNorth` to `True` if `X` axis points to the North
    """
@typing.overload
def TvdXY2MdAzIncl(M: numpy.ndarray[numpy.float64, _Shape[m, n]], x0: float, y0: float, XNorth: bool) -> numpy.ndarray[numpy.float64, _Shape[m, n]]:
    pass
@typing.overload
def TvdXY2MdXYTvd(M: numpy.ndarray[numpy.float32, _Shape[m, n]], x0: float, y0: float, XNorth: bool) -> numpy.ndarray[numpy.float32, _Shape[m, n]]:
    """
    Convert matrix `M` (whose columns represent TVD X Y respectively)to `MD_X_Y_TVD`. Set `XNorth` to `True` if `X` axis points to the North
    """
@typing.overload
def TvdXY2MdXYTvd(M: numpy.ndarray[numpy.float64, _Shape[m, n]], x0: float, y0: float, XNorth: bool) -> numpy.ndarray[numpy.float64, _Shape[m, n]]:
    pass
@typing.overload
def TvdssDxDy2ALL(M: numpy.ndarray[numpy.float32, _Shape[m, n]], x0: float, y0: float, kb: float, XNorth: bool) -> numpy.ndarray[numpy.float32, _Shape[m, n]]:
    """
    Convert matrix `M` (whose columns represent TVDSS DX DY respectively)to `MD_X_Y_Z_TVD_DX_DY_AZ_INCL` (Z the same as TVDSS). Set `XNorth` to `True` if `X` axis points to the North
    """
@typing.overload
def TvdssDxDy2ALL(M: numpy.ndarray[numpy.float64, _Shape[m, n]], x0: float, y0: float, kb: float, XNorth: bool) -> numpy.ndarray[numpy.float64, _Shape[m, n]]:
    pass
@typing.overload
def TvdssDxDy2MdAzIncl(M: numpy.ndarray[numpy.float32, _Shape[m, n]], kb: float, XNorth: bool) -> numpy.ndarray[numpy.float32, _Shape[m, n]]:
    """
    Convert matrix `M` (whose columns represent TVDSS DX DY respectively)to `MD_Az_Incl`. Set `XNorth` to `True` if `X` axis points to the North
    """
@typing.overload
def TvdssDxDy2MdAzIncl(M: numpy.ndarray[numpy.float64, _Shape[m, n]], kb: float, XNorth: bool) -> numpy.ndarray[numpy.float64, _Shape[m, n]]:
    pass
@typing.overload
def TvdssDxDy2MdXYTvd(M: numpy.ndarray[numpy.float32, _Shape[m, n]], x0: float, y0: float, kb: float, XNorth: bool) -> numpy.ndarray[numpy.float32, _Shape[m, n]]:
    """
    Convert matrix `M` (whose columns represent TVDSS DX DY respectively)to `MD_X_Y_TVD`. Set `XNorth` to `True` if `X` axis points to the North
    """
@typing.overload
def TvdssDxDy2MdXYTvd(M: numpy.ndarray[numpy.float64, _Shape[m, n]], x0: float, y0: float, kb: float, XNorth: bool) -> numpy.ndarray[numpy.float64, _Shape[m, n]]:
    pass
def TvdssXY2ALL(M: numpy.ndarray[numpy.float32, _Shape[m, n]], x0: float, y0: float, kb: float, XNorth: bool) -> numpy.ndarray[numpy.float32, _Shape[m, n]]:
    """
    Convert matrix `M` (whose columns represent TVDSS X Y respectively)to `MD_X_Y_Z_TVD_DX_DY_AZ_INCL` (Z the same as TVDSS). Set `XNorth` to `True` if `X` axis points to the North
    """
@typing.overload
def TvdssXY2MdAzIncl(M: numpy.ndarray[numpy.float32, _Shape[m, n]], x0: float, y0: float, kb: float, XNorth: bool) -> numpy.ndarray[numpy.float32, _Shape[m, n]]:
    """
    Convert matrix `M` (whose columns represent TVDSS X Y respectively)to `MD_Az_Incl`. Set `XNorth` to `True` if `X` axis points to the North
    """
@typing.overload
def TvdssXY2MdAzIncl(M: numpy.ndarray[numpy.float64, _Shape[m, n]], x0: float, y0: float, kb: float, XNorth: bool) -> numpy.ndarray[numpy.float64, _Shape[m, n]]:
    pass
@typing.overload
def TvdssXY2MdXYTvd(M: numpy.ndarray[numpy.float32, _Shape[m, n]], x0: float, y0: float, kb: float, XNorth: bool) -> numpy.ndarray[numpy.float32, _Shape[m, n]]:
    """
    Convert matrix `M` (whose columns represent TVDSS X Y respectively)to `MD_X_Y_TVD`. Set `XNorth` to `True` if `X` axis points to the North
    """
@typing.overload
def TvdssXY2MdXYTvd(M: numpy.ndarray[numpy.float64, _Shape[m, n]], x0: float, y0: float, kb: float, XNorth: bool) -> numpy.ndarray[numpy.float64, _Shape[m, n]]:
    pass
def createSeisContainer(arg0: h5gtpy._h5gt.File, arg1: CreationType) -> _H5SeisContainer:
    pass
def createSeisContainerByName(arg0: str, arg1: CreationType) -> _H5SeisContainer:
    pass
def createSurfContainer(arg0: h5gtpy._h5gt.File, arg1: CreationType) -> _H5SurfContainer:
    pass
def createSurfContainerByName(arg0: str, arg1: CreationType) -> _H5SurfContainer:
    pass
def createWellContainer(arg0: h5gtpy._h5gt.File, arg1: CreationType) -> _H5WellContainer:
    pass
def createWellContainerByName(arg0: str, arg1: CreationType) -> _H5WellContainer:
    pass
def openBaseContainer(arg0: h5gtpy._h5gt.File) -> _H5BaseContainer:
    pass
def openBaseContainerByName(arg0: str) -> _H5BaseContainer:
    pass
def openBaseObject(arg0: h5gtpy._h5gt.Group) -> _H5BaseObject:
    pass
def openSeisContainer(arg0: h5gtpy._h5gt.File) -> _H5SeisContainer:
    pass
def openSeisContainerByName(arg0: str) -> _H5SeisContainer:
    pass
def openSurfContainerByName(arg0: str) -> _H5SurfContainer:
    pass
def openWellContainer(arg0: h5gtpy._h5gt.File) -> _H5WellContainer:
    pass
def openWellContainerByName(arg0: str) -> _H5WellContainer:
    pass
@typing.overload
def quickHull2D(M: numpy.ndarray[numpy.float32, _Shape[m, 2]]) -> numpy.ndarray[numpy.float32, _Shape[m, 2]]:
    """
    Quick Hull 2D algorithm https://en.wikipedia.org/wiki/quickHull. `M` is a two column matrix: first col - X, second - Y. Return two column matrix (XY)
    """
@typing.overload
def quickHull2D(M: numpy.ndarray[numpy.float64, _Shape[m, 2]]) -> numpy.ndarray[numpy.float64, _Shape[m, 2]]:
    pass
@typing.overload
def sort(v: numpy.ndarray[numpy.float32, _Shape[m, 1]]) -> typing.Tuple[numpy.ndarray[numpy.int64, _Shape[m, 1]], numpy.ndarray[numpy.float32, _Shape[m, 1]]]:
    """
    return indices such that `v_sorted = v(ind)`. Input parameter `v` is a vector

    return indices such that `v_sorted = v(ind)` and also return `v_sorted`. Input parameter `v` is a vector
    """
@typing.overload
def sort(v: numpy.ndarray[numpy.float32, _Shape[m, 1]]) -> numpy.ndarray[numpy.int64, _Shape[m, 1]]:
    pass
@typing.overload
def sort(v: numpy.ndarray[numpy.float64, _Shape[m, 1]]) -> typing.Tuple[numpy.ndarray[numpy.int64, _Shape[m, 1]], numpy.ndarray[numpy.float64, _Shape[m, 1]]]:
    pass
@typing.overload
def sort(v: numpy.ndarray[numpy.float64, _Shape[m, 1]]) -> numpy.ndarray[numpy.int64, _Shape[m, 1]]:
    pass
@typing.overload
def sort_rows(M: numpy.ndarray[numpy.float32, _Shape[m, n]]) -> numpy.ndarray[numpy.int64, _Shape[m, 1]]:
    """
    sorts the rows of a matrix in ascending order based on the elements in the first column. When the first column contains repeated elements, sortrows sorts according to the values in the next column and repeats this behavior for succeeding equal values. M_sorted = M(ind, Eigen::all)

    sorts the rows of a matrix in ascending order based on the elements in the first column. When the first column contains repeated elements, sortrows sorts according to the values in the next column and repeats this behavior for succeeding equal values. also calculates M_sorted = M(ind, Eigen::all)
    """
@typing.overload
def sort_rows(M: numpy.ndarray[numpy.float32, _Shape[m, n]]) -> typing.Tuple[numpy.ndarray[numpy.int64, _Shape[m, 1]], numpy.ndarray[numpy.float32, _Shape[m, n]]]:
    pass
@typing.overload
def sort_rows(M: numpy.ndarray[numpy.float64, _Shape[m, n]]) -> numpy.ndarray[numpy.int64, _Shape[m, 1]]:
    pass
@typing.overload
def sort_rows(M: numpy.ndarray[numpy.float64, _Shape[m, n]]) -> typing.Tuple[numpy.ndarray[numpy.int64, _Shape[m, 1]], numpy.ndarray[numpy.float64, _Shape[m, n]]]:
    pass
@typing.overload
def sort_rows_unique(M: numpy.ndarray[numpy.float32, _Shape[m, n]]) -> typing.Tuple[numpy.ndarray[numpy.int64, _Shape[m, 1]], numpy.ndarray[numpy.float32, _Shape[m, n]], numpy.ndarray[numpy.int64, _Shape[m, 2]]]:
    """
    find unique rows, sort them, identify unique rows start and end row-indices and return row-indices such that M_sorted = M(ind, Eigen::all).Return indices `ind`, `urows` and `urows_from_size`

    find unique rows, sort them, identify unique rows start and end row-indices and return row-indices such that M_sorted = M(ind, Eigen::all).Return indices `ind`, `urows` and `urows_from_size`. Also return `M_sorted`
    """
@typing.overload
def sort_rows_unique(M: numpy.ndarray[numpy.float32, _Shape[m, n]]) -> typing.Tuple[numpy.ndarray[numpy.int64, _Shape[m, 1]], numpy.ndarray[numpy.float32, _Shape[m, n]], numpy.ndarray[numpy.int64, _Shape[m, 2]], numpy.ndarray[numpy.float32, _Shape[m, n]]]:
    pass
@typing.overload
def sort_rows_unique(M: numpy.ndarray[numpy.float64, _Shape[m, n]]) -> typing.Tuple[numpy.ndarray[numpy.int64, _Shape[m, 1]], numpy.ndarray[numpy.float64, _Shape[m, n]], numpy.ndarray[numpy.int64, _Shape[m, 2]]]:
    pass
@typing.overload
def sort_rows_unique(M: numpy.ndarray[numpy.float64, _Shape[m, n]]) -> typing.Tuple[numpy.ndarray[numpy.int64, _Shape[m, 1]], numpy.ndarray[numpy.float64, _Shape[m, n]], numpy.ndarray[numpy.int64, _Shape[m, 2]], numpy.ndarray[numpy.float64, _Shape[m, n]]]:
    pass
@typing.overload
def sort_unique(v: numpy.ndarray[numpy.float32, _Shape[m, 1]]) -> typing.Tuple[numpy.ndarray[numpy.int64, _Shape[m, 1]], numpy.ndarray[numpy.float32, _Shape[m, 1]], numpy.ndarray[numpy.int64, _Shape[m, 2]]]:
    """
    find unique elements, sort them, identify unique values start and end indices and return indices `ind` such that v_sorted = v(ind), `uvals` vector and two column matrix `uvals_from_size` wherefirst col - start index, second col - number of elements. Each row can be considered as v_sorted.segment(uvals_from_size.row(n)) gives the same unique value uval.

    find unique elements, sort them, identify unique values start and end indices and return indices `ind` such that v_sorted = v(ind), `uvals` vector and two column matrix `uvals_from_size` wherefirst col - start index, second col - number of elements. Each row can be considered as v_sorted.segment(uvals_from_size.row(n)) gives the same unique value uval. Also return `v_sorted`
    """
@typing.overload
def sort_unique(v: numpy.ndarray[numpy.float32, _Shape[m, 1]]) -> typing.Tuple[numpy.ndarray[numpy.int64, _Shape[m, 1]], numpy.ndarray[numpy.float32, _Shape[m, 1]], numpy.ndarray[numpy.int64, _Shape[m, 2]], numpy.ndarray[numpy.float32, _Shape[m, 1]]]:
    pass
@typing.overload
def sort_unique(v: numpy.ndarray[numpy.float64, _Shape[m, 1]]) -> typing.Tuple[numpy.ndarray[numpy.int64, _Shape[m, 1]], numpy.ndarray[numpy.float64, _Shape[m, 1]], numpy.ndarray[numpy.int64, _Shape[m, 2]], numpy.ndarray[numpy.float64, _Shape[m, 1]]]:
    pass
@typing.overload
def sort_unique(v: numpy.ndarray[numpy.float64, _Shape[m, 1]]) -> typing.Tuple[numpy.ndarray[numpy.int64, _Shape[m, 1]], numpy.ndarray[numpy.float64, _Shape[m, 1]], numpy.ndarray[numpy.int64, _Shape[m, 2]]]:
    pass