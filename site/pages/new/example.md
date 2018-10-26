why tar?
  because it is a convenient way for people who receive a file with many
  parts to unpack it automatically into its component parts properly named
  (without messy cutting and pasting).
why compress?
  because filesizes are typically reduced by at least a factor of two
why uuencode?
  because compressed files are binary and will be corrupted when sent via
  e-mail. (uuencode translates to ascii specifically for e-mail transmission.
  note that raw postscript as well can be corrupted by e-mail transmission
  due to occasional long lines or entry into bitmap mode --- uuencoding
 [after compression, since .ps tends to compress well] eliminates any problems)
