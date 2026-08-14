# External order-type database provenance

Retrieved 2026-08-13 from the Aichholzer--Aurenhammer--Krasser order-type
database at

`http://www.ist.tugraz.at/staff/aichholzer/research/rp/triangulations/ordertypes/`

The large binary files are deliberately **not vendored**.  The provider's
`readme.txt` says that the coordinate files contain one representative of
each inequivalent realizable general-position order type, with one member of
each reflection pair retained.  It gives counts 3,315 for eight points and
158,817 for nine points, exactly matching the record counts read here.  It
also describes the little-endian coordinate formats and the database's
completeness audit.  The readme permits free noncommercial,
nongovernmental, nonmilitary use and asks users to notify the maintainers of
investigations; other uses require contacting them.  Anyone publishing these
finite results should contact/cite the database authors as requested.

## Retrieved-file manifest

| file | bytes | SHA-256 |
|---|---:|---|
| `otypes08.b08` | 53,040 | `d4a5756295a584a57962fca946b4021cbe5c257481b0bc731ef081d1ca2ea0bd` |
| `otypes09.b16` | 5,717,412 | `e48faf76c3890ef5481b043bc681b05052b2015092837549b2c53e18626038b4` |
| `kgons08.b08` | 19,890 | `6e0e159312e7bf1164bc9e3b409596e21cefccdc65437c8b728fb17e6434dc3f` |
| `kgons09.b08` | 1,111,719 | `0e2b5d3e1b3128b5f6fb54f5d29d5460462ae2bb4f7320ae19f5c31ec9de7701` |
| `crossn08.b08` | 3,315 | `8ad58e9d7af424d221b7c325f8bc67964ac3b149b10d6e797e0c3b45ff227d96` |
| `crossn09.b08` | 158,817 | `361bc8857c15d1508d111035e4c20194fd3efa25d380197345e435afca205f22` |
| `readme.txt` | 7,280 | `f3dc2dce102a0f7373247c9617bc83562c43b28770184f7525c5826887033526` |
| `applications.txt` | 14,168 | `2c5f14b8bf40e97393faedc29e870242f680a082c33a412a682cd42f477780a2` |

The coordinate scan in `scan_order_types.cpp` recomputes every rank
polynomial by endpoint cap--cup factorization.  Independently,
`verify_database_profiles.py` scans the provider's aligned `kgons` records.
The two full scans agree on the minimum values, multiplicities, profiles, and
record indices.  Finally, `direct_hull_verify.py` ignores both matrix methods
and enumerates all subsets of the two winning integer configurations using a
direct monotone-chain convex-hull test.

## Why the scan covers the geometric problem

The number of convex subsets and their size profile depend only on the order
type and are unchanged by relabeling or reflection.  Consequently one member
of each inequivalent realizable order type/reflection pair suffices.  Every
finite planar general-position point set has one of those realizable order
types.  Subject to the database's documented completeness theorem, scanning
all 3,315 or 158,817 records is therefore exhaustive over actual point sets,
not merely over the displayed coordinate representatives.

Primary database references listed by the provider are:

1. O. Aichholzer, F. Aurenhammer, and H. Krasser, *Enumerating Order Types
   for Small Point Sets with Applications*, SoCG 2001 / Order 19 (2002).
2. O. Aichholzer and H. Krasser, *The Point Set Order Type Data Base: A
   Collection of Applications and Results*, CCCG 2001.
3. O. Aichholzer and H. Krasser, *Abstract order type extension and new
   results on the rectilinear crossing number*, Computational Geometry 36
   (2006), 2--15.
