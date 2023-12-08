from lib.filter import Filter

if __name__ == "__main__":
    filter = Filter()
    filter.head_set("demo-var-0", str)
    filter.head_set("demo-var-1", str)
    print(filter.table_get())
