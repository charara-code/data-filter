import argparse
from .data_loader.factory import Factory
from .stats.csv_stats import CSVStats
from .stats.json_stats import JSONStats
from .models.data_containers.json_data_container import JsonDataContainer
from .sorter.csv_sorter import CSVSorter
from .sorter.json_sorter import JsonSorter
from .filter.csv_filter import CSVFilter
from .filter.json_filter import JSONFilter


def create_cli():
    data = None
    file_type = None
    while True:
        parser = argparse.ArgumentParser(description="Data Filter CLI Application")
        parser.add_argument(
            "--version", action="version", version="Data Filter CLI 1.0"
        )
        subparsers = parser.add_subparsers(dest="command", help="Sub-command help")

        # loading data
        load_parser = subparsers.add_parser("load", help="Load data")
        load_parser.add_argument("file", type=str, help="Path to the data file")
        # load_parser.add_argument('type', type=str, choices=['csv', 'json'], help='Type of the data file (csv or json)')

        # stats command
        stats_parser = subparsers.add_parser("stats", help="Display statistics")

        # sort command
        sort_parser = subparsers.add_parser("sort", help="Sort data")
        sort_parser.add_argument("file", type=str, help="Path to the data file")
        sort_parser.add_argument("key", type=str, help="Key/Column to sort by")
        sort_parser.add_argument(
            "--reverse", action="store_true", help="Sort in descending order"
        )

        # filter command
        filter_parser = subparsers.add_parser("filter", help="Filter data")
        # filter_parser.add_argument('file', type=str, help='Path to the data file')
        filter_parser.add_argument("column", type=str, help="Column/Key to filter by")
        filter_parser.add_argument("value", type=str, help="Value to filter by")
        filter_parser.add_argument(
            "--comparison",
            type=str,
            choices=["eq", "lt", "gt"],
            default="eq",
            help="Comparison type",
        )

        # display parser
        display_parser = subparsers.add_parser("display", help="Display data")

        exit_parser = subparsers.add_parser("exit", help="Exit the CLI")

        args = parser.parse_args(input("Enter command: ").split())

        if args.command is None:
            parser.print_help()
        else:
            if args.command == "load":
                data = load_data(args.file)
                file_type = args.file.split(".")[-1]
            elif args.command == "stats":
                if data is None:
                    print("Data not loaded. Please load data first.")
                else:
                    display_stats(data, loader_name=file_type)
            elif args.command == "sort":
                if data is None:
                    print("Data not loaded. Please load data first.")
                else:
                    sort_data(
                        data, loader_name=file_type, key=args.key, reverse=args.reverse
                    )
            elif args.command == "filter":
                if data is None:
                    print("Data not loaded. Please load data first.")
                else:
                    # attempt to convert the value to an integer, float, or boolean
                    try:
                        value = int(args.value)
                    except ValueError:
                        try:
                            value = float(args.value)
                        except ValueError:
                            if args.value.lower() == "true":
                                value = True
                            elif args.value.lower() == "false":
                                value = False
                            else:
                                value = args.value
                    filter_data(
                        data,
                        loader_name=file_type,
                        column=args.column,
                        value=value,
                        comparison=args.comparison,
                    )
            elif args.command == "display":
                if data is None:
                    print("Data not loaded. Please load data first.")
                else:
                    if file_type == "csv":
                        print(data.head(-1))
                    elif file_type == "json":
                        pretty_print_json(data)
            elif args.command == "exit":
                print("Exiting the CLI.")
                break


def pretty_print_json(data: JsonDataContainer):
    """
    Pretty print the JSON data.

    Args:
        data (JsonDataContainer): The JSON data to pretty print.
    """
    for item in data.data:
        for key, value in item.item.items():
            print(f"{key}: {value}")
        print()


def load_data(file_path):
    """
    Load data from the specified file path using the specified file type.

    Args:
        file_path (str): The path to the data file.
    """
    try:
        loader_name = file_path.split(".")[-1]
        data_loader = Factory.get_data_loader(
            loader_name=loader_name, data_source=file_path
        )
        data = data_loader.load_data()
        if loader_name == "csv":
            print(data.head(-1))
        elif loader_name == "json":
            pretty_print_json(data)
        print(f"Loaded {loader_name.upper()} data from {file_path}:")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")


def display_stats(data, loader_name):
    """
    Display statistics for the specified data file.

    Args:
        data: The data to display statistics for.
        loader_name (str): The type of the data file (csv or json).
    """
    try:
        if loader_name == "csv":
            stats = CSVStats(data)
        elif loader_name == "json":
            stats = JSONStats(data)
        else:
            raise ValueError(f"Unsupported file type: {loader_name}")

        all_stats = stats.get_all_stats()
        # unpack the dictionary and display the stats
        for key, value in all_stats.items():
            print(f"{key.capitalize()} statistics:")
            for field, field_stats in value.items():
                print(f"  {field.capitalize()}:")
                for stat, stat_value in field_stats.items():
                    print(f"    {stat.replace('_', ' ').capitalize()}: {stat_value}")
    except Exception as e:
        print(f"Error displaying stats: {e}")


def sort_data(data, loader_name, key, reverse):
    """
    Sort the data by the specified key.

    Args:
        data: The data to sort.
        loader_name (str): The type of the data file (csv or json).
        key (str): The key/column to sort by.
        reverse (bool): Whether to sort in descending order.
    """
    try:
        if loader_name == "csv":
            sorter = CSVSorter(data)
            sorter.sort_by_column(key, ascending=not reverse)
            sorted_data = sorter.get_sorted_dataframe()
            print(sorted_data.head(-1))
        elif loader_name == "json":
            sorter = JsonSorter(data)
            sorter.sort_by_key(key, reverse=reverse)
            sorted_data = sorter.get_sorted_data()
            pretty_print_json(sorted_data)
        else:
            raise ValueError(f"Unsupported file type: {loader_name}")
    except Exception as e:
        print(f"Error sorting data: {e}")


def filter_data(data, loader_name, column, value, comparison):
    """
    Filter the data by the specified column and value.

    Args:
        data: The data to filter.
        loader_name (str): The type of the data file (csv or json).
        column (str): The column/key to filter by.
        value (str): The value to filter by.
        comparison (str): The type of comparison ('eq', 'lt', 'gt').
    """
    try:
        if loader_name == "csv":
            filterer = CSVFilter(data)
            filterer.filter_by_column(column, value, comparison=comparison)
            filtered_data = filterer.get_filtered_dataframe()
            print(filtered_data.head(-1))
        elif loader_name == "json":
            filterer = JSONFilter(data)
            filterer.filter_by_key(column, value, comparison=comparison)
            filtered_data = filterer.get_filtered_data()
            pretty_print_json(filtered_data)
        else:
            raise ValueError(f"Unsupported file type: {loader_name}")
    except Exception as e:
        print(f"Error filtering data: {e}")
