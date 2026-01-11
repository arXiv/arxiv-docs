# Creating `tar.gz` and `zip` Files

Many submissions have multiple files and are much more convenient to
upload if packaged in a single file. Two good utilities for doing this
are [tar](#tar) and [zip](#zip).

Note that arXiv does not currently support `rar` archives, or `bz` or
`bz2` compression. Also, you must not simply concatenate files together
since arXiv will have no way of sensibly unpacking them.

### <span id="tar">`tar` files</span>

The utility `tar` (for Tape ARchive) is a good way to package up
multiple files into a single package. `tar` is available for all
platforms and is installed by default on most Linux/Unix systems and on
Macs with OSX. See our [discussion of availability and
installation](utilities.md#taretc).

`tar` files have a `.tar` extension

On the Unix command line, you create a tar archive as follows. Suppose
you have several files, `foo.tex`, `fig1.eps`, `fig2.eps`. Then the
following creates a tar file called `mystuff.tar` including those files:

      $ tar -cvf mystuff.tar foo.tex fig1.eps fig2.eps

**Warning:** If you forget to type the filename `mystuff.tar`, tar will
over-write the first file name it sees (in this case `foo.tex` is next
in line). Isn't Unix fun?

You will then want to use [gzip](gzip.md) to compress the tar file for
fastest upload:

      $ gzip mystuff.tar

which will create a file named `mystuff.tar.gz`.

Alternately, most versions of tar allow you to create a gzipped tar file
in one action. Using the above example, to create a gzipped tar file
called `mystuff.tar.gz`, do the following:

      $ tar -cvzf mystuff.tar.gz foo.tex fig1.eps fig2.eps

### <span id="zip">`zip` files</span>

Various utilities can produce `zip` files. These include WinZip on
Windows systems and Zip, StuffIt (commercial version) on Mac systems.
`zip` files provide a way to both package multiple files and compress
the result and so are essentially equivalent to `.tar.gz` files.

### Unpacking a .tar.gz file

See our [unpacking help page](unpack.md) for information on unpacking
`.tar.gz` files.
