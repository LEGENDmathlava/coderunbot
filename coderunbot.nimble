# Package

version       = "0.1.0"
author        = "Gart2357"
description   = "Runnig your code on Discord"
license       = "AGPL-3.0"
srcDir        = "src"
bin           = @["coderunbot"]



# Dependencies

requires "nim >= 1.2.0", "dimscord#head", "dotenv >= 1.1.0"