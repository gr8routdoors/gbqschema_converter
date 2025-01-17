# Dmitry Kisler © 2020
# www.dkisler.com

import sys
import time
import argparse
import json
from gbqschema_converter.jsonschema_to_gbqschema import json_representation as to_gbq
from gbqschema_converter.gbqschema_to_jsonschema import json_representation as to_json
from gbqschema_converter.logger import get_logger


logs = get_logger()
help_string = "Google BigQuery Table Schema Converter"


def get_args() -> argparse.Namespace:
    """CL input parameters."""
    parser = argparse.ArgumentParser(description=help_string)
    required_either = parser.add_mutually_exclusive_group(required=True)
    required_either.add_argument('-i', '--input', 
                                 help="Input object as string.",
                                 type=str, 
                                 default=None)
    required_either.add_argument('-f', '--file',
                                 help="Input object as file path.",
                                 type=str,
                                 default=None)
    args = parser.parse_args()
    return args


def _input() -> dict:
    """Input parser.
    
    Returns:
      
      Input schema.
    """
    args = get_args()

    if args.file:
        try:
            with open(args.file, 'r') as f:
                schema_in = json.load(f)
        except IOError as ex:
            logs.error(f"File reading error: {ex}")
            sys.exit(1)
        except Exception as ex:
            logs.error(f"Input parsing error: {ex}")
            sys.exit(1)
    else:
        try:
            schema_in = json.loads(args.input)
        except Exception as ex:
            logs.error(f"Input parsing error: {ex}")
            sys.exit(1)
    return schema_in


def json_to_gbq():
    try:
        t0 = time.time()
        schema_out = to_gbq(_input())
        logs.info(f"""Output ({round((time.time() - t0) * 1000, 2)} ms elapsed):  SUCCESS""")
        print(json.dumps(schema_out, indent=2))
    except Exception as ex:
        logs.error(f"Schema conversion error: {ex}")
        raise ex
        sys.exit(1)    


def gbq_to_json():
    try:
        t0 = time.time()
        schema_out = to_json(_input())
        logs.info(f"""Output ({round((time.time() - t0) * 1000, 2)} ms elapsed):  SUCCESS""")
        print(json.dumps(schema_out, indent=2))
    except Exception as ex:
        logs.error(f"Schema conversion error: {ex}")
        sys.exit(1)
