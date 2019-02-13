Type 1 PostScript fonts on Linux
================================

Most recent linux distributions come with teTeX, TeXLive, or similar,
and therefore already have the necessary type 1 fonts. All that is
required to display PostScript files with type 1 fonts with
ghostscript/ghostview/gv are two small configuration changes.

Make a symbolic link from the location of the type 1 fonts in the
teTeX/texmf tree to the ghostscript font directory, e.g.

    % ln -s $TETEXROOT/texmf/fonts/type1/bluesky /usr/share/ghostscript/fonts
    % ln -s $TETEXROOT/texmf/fonts/type1/hoekwater /usr/share/ghostscript/fonts

Next, edit the ghostscript fontmap, typically (replace x.xx with the
correct version)

    /usr/local/share/ghostscript/x.xx/lib/Fontmap.GS

to recognize these fonts by adding an entry of the following form for
each `.pfb` file found in subdirectories of:

    /usr/local/share/ghostscript/fonts/bluesky/
    /usr/local/share/ghostscript/fonts/hoekwater/

for example,

    %
    % Bluesky tye I cm fonts in .pfb form from teTeX
    %
    /cmb10          (bluesky/cm/cmb10.pfb)          ;
    /cmbsy10        (bluesky/cm/cmbsy10.pfb)    ;
    /cmbx10         (bluesky/cm/cmbx10.pfb)         ;

    etc.

Recent gs (\> 8.6x) uses compile time font information by default. To
have the above modifications take effect, either re-compile gs with the
extended fontmap, or use the commandline option -sFONTMAP=\<filename\>
