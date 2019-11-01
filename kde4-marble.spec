# TODO:
# -- The following OPTIONAL packages have not been found:
#
# * QextSerialPort , access to serial ports , <http://code.google.com/p/qextserialport/>
#   Reading from serial port in APRS plugin
# * quazip , reading and writing of ZIP archives , <http://quazip.sourceforge.net/>
#   reading and displaying .kmz files
# * libshp , reading and writing of ESRI Shapefiles (.shp) , <http://shapelib.maptools.org/>
#   reading and displaying .shp files
# * liblocation , position information on Maemo 5 devices , <http://maemo.org/>
#   position information via GPS/WLAN for the Nokia N900 smartphone
# * QtMobility , a collection of APIs and frameworks , <http://qt.digia.com/>
#   Required for QtLocation to work
# * QtLocation , geographical support for position and map use , <http://qt.digia.com/>
#   position information via QtMobility QtLocation
# * libwlocate , WLAN-based geolocation , <http://www.openwlanmap.org/>
#   Position information based on neighboring WLAN networks
#
# Conditional build:
#
%define         orgname     marble
%define         _state      stable
%define         qtver       4.8.1
#
Summary:	Marble
Summary(pl.UTF-8):	Marble
Name:		kde4-marble
Version:	4.14.3
Release:	7
License:	LGPL v2
Group:		X11/Libraries
Source0:	http://download.kde.org/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	c102d058423e0cee1ee964eebe6ac6c2
URL:		http://www.kde.org/
# leave only required ones
BuildRequires:	Qt3Support-devel >= %{qt_ver}
BuildRequires:	QtCore-devel >= %{qt_ver}
BuildRequires:	QtDBus-devel >= %{qt_ver}
BuildRequires:	QtDesigner-devel >= %{qt_ver}
BuildRequires:	QtGui-devel >= %{qt_ver}
BuildRequires:	QtScript-devel >= %{qt_ver}
BuildRequires:	QtSvg-devel >= %{qt_ver}
BuildRequires:	QtTest-devel >= %{qt_ver}
BuildRequires:	QtUiTools-devel >= %{qt_ver}
BuildRequires:	QtWebKit-devel
BuildRequires:	QtXml-devel >= %{qt_ver}
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.6.3
BuildRequires:	gpsd-devel >= 2.37
BuildRequires:	kde4-kdelibs-devel >= %{_kdever}
BuildRequires:	phonon-devel >= 4.3.1
BuildRequires:	pkgconfig
BuildRequires:	qt4-build >= %{qt_ver}
BuildRequires:	qt4-qmake >= %{qt_ver}
BuildRequires:	rpmbuild(macros) >= 1.293
BuildRequires:	shapelib-devel
Obsoletes:	kde4-kdeedu-marble < 4.6.99
Obsoletes:	marble <= 4.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Marble is a Virtual Globe and World Atlas that you can use to learn
more about Earth: You can pan and zoom around and you can look up
places and roads. A mouse click on a place label will provide the
respective Wikipedia article.

%description -l pl.UTF-8
Marble.

%package devel
Summary:	Marble header files
Summary(pl.UTF-8):	Pliki nagłówkowe dla Marble
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	kde4-kdelibs-devel >= %{version}
Obsoletes:	kde4-kdeedu-devel < 4.6.99
Obsoletes:	marble-devel <= 4.8.0

%description devel
This package contains Marble header files.

%description devel -l pl.UTF-8
Pakiet zawiera pliki nagłówkowe dla Marble.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{orgname} --with-kde

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{orgname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/marble
%attr(755,root,root) %{_bindir}/marble-mobile
%attr(755,root,root) %{_bindir}/marble-qt
%attr(755,root,root) %{_bindir}/marble-touch
#%attr(755,root,root) %{_bindir}/routing-instructions
#%attr(755,root,root) %{_bindir}/tilecreator
%attr(755,root,root) %{_libdir}/kde4/libmarble_part.so
%attr(755,root,root) %{_libdir}/kde4/marblethumbnail.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_worldclock.so
%attr(755,root,root) %{_libdir}/kde4/plasma_runner_marble.so
%attr(755,root,root) %{_libdir}/kde4/plugins/designer/LatLonEditPlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/designer/MarbleNavigatorPlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/designer/MarbleWidgetPlugin.so
%dir %{_libdir}/kde4/plugins/marble
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/AnnotatePlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/AprsPlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/AtmospherePlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/CachePlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/CompassFloatItem.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/CrosshairsPlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/CycleStreetsPlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/EarthquakePlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/EclipsesPlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/ElevationProfileFloatItem.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/ElevationProfileMarker.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/FlightGearPositionProviderPlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/FoursquarePlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/GpsbabelPlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/GosmoreReverseGeocodingPlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/GosmoreRoutingPlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/GpsdPositionProviderPlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/GpsInfo.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/GpxPlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/GraticulePlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/HostipPlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/JsonPlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/KmlPlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/LatLonPlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/License.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/LocalDatabasePlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/LocalOsmSearchPlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/LogPlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/MapQuestPlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/MapScaleFloatItem.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/MeasureTool.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/MonavPlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/NavigationFloatItem.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/NominatimReverseGeocodingPlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/NominatimSearchPlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/OpenCachingComPlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/OpenDesktopPlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/OpenRouteServicePlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/OsmPlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/OSRMPlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/OverviewMap.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/Photo.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/PlacemarkPositionProviderPlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/Pn2Plugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/PntPlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/PositionMarker.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/PostalCode.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/ProgressFloatItem.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/RouteSimulationPositionProviderPlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/RoutingPlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/RoutinoPlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/SatellitesPlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/ShpPlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/Speedometer.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/StarsPlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/SunPlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/Weather.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/Wikipedia.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/YoursPlugin.so
%attr(755,root,root) %ghost %{_libdir}/libmarblewidget.so.??
%attr(755,root,root) %{_libdir}/libmarblewidget.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libastro.so.?
%attr(755,root,root) %{_libdir}/libastro.so.*.*.*
%{_desktopdir}/kde4/marble.desktop
%{_desktopdir}/kde4/marble_geo.desktop
%{_desktopdir}/kde4/marble_gpx.desktop
%{_desktopdir}/kde4/marble_kml.desktop
%{_desktopdir}/kde4/marble-mobile.desktop
%{_desktopdir}/kde4/marble_osm.desktop
%{_desktopdir}/kde4/marble-qt.desktop
%{_desktopdir}/kde4/marble_shp.desktop
%{_desktopdir}/kde4/marble-touch.desktop
%{_desktopdir}/kde4/marble_worldwind.desktop
%{_datadir}/appdata/marble.appdata.xml
%{_datadir}/apps/marble
%{_datadir}/config.kcfg/marble.kcfg
%{_datadir}/kde4/services/marble_part.desktop
%{_datadir}/kde4/services/marble_part_gpx.desktop
%{_datadir}/kde4/services/marble_part_kml.desktop
%{_datadir}/kde4/services/marble_part_osm.desktop
%{_datadir}/kde4/services/marble_part_shp.desktop
%{_datadir}/kde4/services/marble_thumbnail_gpx.desktop
%{_datadir}/kde4/services/marble_thumbnail_kml.desktop
%{_datadir}/kde4/services/marble_thumbnail_osm.desktop
%{_datadir}/kde4/services/marble_thumbnail_shp.desktop
%{_datadir}/kde4/services/plasma-applet-kworldclock.desktop
%{_datadir}/kde4/services/plasma-runner-marble.desktop
%{_datadir}/mime/packages/geo.xml
%{_iconsdir}/hicolor/*x*/apps/marble.png
%{_libdir}/qt4/imports/org/kde/edu
#%{_libdir}/qt4/imports/org/kde/edu/marble

%files devel
%defattr(644,root,root,755)
%{_includedir}/astro
%{_includedir}/marble
%attr(755,root,root) %{_libdir}/libastro.so
%attr(755,root,root) %{_libdir}/libmarblewidget.so
%{_datadir}/apps/cmake/modules/FindMarble.cmake
