from lib.filter import Filter

if __name__ == "__main__":
    filter = Filter()
    header = {
        "demo_subject": str,
        "demo_verb": str,
        "demo_object": str,
        "demo_nb": int,
    }
    filter_chain = [
        "START",
        "(?P<demo_subject>\w+) (?P<demo_verb>\w+) (?P<demo_object>\w+) .*",
        ".*(?P<demo_nb>\d+).*",
        "END",
    ]
    filter.head_set(header)
    filter.filter_set(filter_chain)
    filter.delim_set(start=True, end=True)

    # demo valid filter
    print("##### Demo simple test #####")
    filter.parse("START")
    filter.parse("This is demo filter: 1")
    filter.parse(". is not valid string 2")
    filter.parse("END")
    print(filter.table_get(), end="\n\n")

    # demo multiple object matching
    print("##### Demo multiple object rows test #####")
    filter.parse("START")
    filter.parse("This is demo filter: 3")
    filter.parse("END")
    filter.parse("START")
    filter.parse("This is demo filter: 4")
    filter.parse("END")
    print(filter.table_get(), end="\n\n")

    # demo no start validate
    print("##### Demo no start line validate #####")
    filter.delim_set(start=False)
    filter.parse("This is demo filter: 5")
    filter.parse("END")
    filter.delim_set(start=True)
    print(filter.table_get(), end="\n\n")

    # demo invalid filter
    print("##### Demo invalid parsing #####")
    try:
        filter.parse("This is a valid string end: 1")
        print(filter.table_get(), end="\n\n")
    except Exception as e:
        print(f"Error in parsing: {e}", end="\n\n")
