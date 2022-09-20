# xhdvi precompiled binaries

xhdvi binaries precompiled for the following machines:

*   for Sun OS 4.1: [xhdvi\_sun\_4.1.tar.gz](xhdvi_sun_4.1.tar.gz)
*   for HPUX 9.05: [xhdvi\_hpux\_9.05.tar.gz](xhdvi_hpux_9.05.tar.gz)
*   for SGI: [xhdvi\_iris\_5.2.tar.gz](xhdvi_iris_5.2.tar.gz)
*   for ibm risc 6000: [xhdvi.RS6000](ftp://snorri.chem.washington.edu/pub/hypertex/xhdvi.RS6000)
*   X on nExtstep (see also the nExtstep native [HyperTeXview](../HyperTeXview.tar.gz)):
    *   [xhdvi.NextIntel](ftp://snorri.chem.washington.edu/pub/hypertex/xhdvi.NextIntel)
    *   [xhdvi.NextNext](ftp://snorri.chem.washington.edu/pub/hypertex/xhdvi.NextNext) (not currently available)

**Warning:** These have been compiled with the following font paths:  

> DEFAULT\_FONT\_PATH=/usr/local/lib/tex/fonts/pk  
> DEFAULT\_SUBDIR\_PATH=/usr/local/lib/tex/fonts/\*\*  
> DEFAULT\_VF\_PATH=/usr/local/lib/tex/fonts/vf

If your fonts reside in a different location, you either need to install a symbolic link, e.g.  

```bash
ln -s /some/font/directory /usr/local/lib/tex/fonts/pk
```

or set the environment variables, e.g.  
```bash
export XDVIFONTS=/some/font/directory
```
(The environment variables corresponding to the other two above precompiled options are `TEXFONTS\_SUBDIR` and `XDVIVFS` )

If all else fails, return to the [xhdvi source](/help/hypertex/index.md#xhdvisource)

### Return to [HyperTeX](/help/hypertex/index.md)