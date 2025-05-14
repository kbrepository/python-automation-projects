import argparse
from utils.file_handler import add_expense, show_summary, export_to_json
import logging

# Logging setup
logging.basicConfig(filename='logs/tracker.log', level=logging.INFO, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

def main():
    parser = argparse.ArgumentParser(description='Simple CLI Expense Tracker')
    subparsers = parser.add_subparsers(dest='command')

    # Add expense command
    add_parser = subparsers.add_parser('add')
    add_parser.add_argument('--date', required=True)
    add_parser.add_argument('--category', required=True)
    add_parser.add_argument('--amount', type=float, required=True)
    add_parser.add_argument('--note', default='')

    # Show summary
    subparsers.add_parser('summary')

    # Export to JSON
    subparsers.add_parser('export')

    args = parser.parse_args()

    if args.command == 'add':
        add_expense(args.date, args.category, args.amount, args.note)
    elif args.command == 'summary':
        show_summary()
    elif args.command == 'export':
        export_to_json()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
