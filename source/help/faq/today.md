# Why Does My Paper Give the Wrong Date?

If you have a LaTeX submission that uses the `\today` macro to get the date, either explicitly or by default from a style file, then this will show the date the file was processed. We do not store the PS or PDF generated from LaTeX submissions long-term. Instead, we generate these formats from the source when they are requested (the output is cached for a time that depends on availability of space and access pattern). Thus the source will likely be processed at different times after the initial submission and dates created with the `\today` macro will reflect this.

Solution
--------

Do not use the `\today` macro, and correctly override default dates supplied by style files.

We consider the date stamped on the left hand side of the page, along with the paper identifier, to be definitive. Dates in the paper are supplied by the submitter and we have no control over them. We have considered overriding the `\today` macro, but believe that this would cause more problems than it cures. The correct solution is as noted above.
