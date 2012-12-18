package test


describe "Tests type inference of the table columns"{
	def myTable {
		| MyEnum value   |
		| MyEnum::VALUE1 |
		| MyEnum::VALUE2 |
    }		
	
	fact "Table column type get inferred by the stand-alone compile correctly" {
		myTable.forEach [
			acceptPruefungsArt(value)
			throw new RuntimeException
		]
	}
	
	def acceptPruefungsArt(MyEnum myEnum) {
		
	}
}