from lib.filter import Filter

if __name__ == "__main__":
    filter = Filter()
    header = {"demo_var_0": str, "demo_var_1": str}
    filter_chain = [
        "This is (?P<demo_var_0>\w+) .*",
    ]
    filter.head_set(header)
    filter.filter_set(filter_chain)

    filter.parse("This is demo filter")

    print(filter.table_get())
