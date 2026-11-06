import subprocess
import sys
import logging

#configure logging
logging.basicConfig(
    filename="pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

steps = [
         "pipeline.py",
         "load_to_sql.py",
         "sql_analytics.py"
         ]

logging.info("Retail Sales Pipeline Started")

print("==== PIPELINE STARTED ====")


try:
    for step in steps:
        print(f"\nRunning: {step}")

        logging.info(f"Starting {step}")

        subprocess.run(
            [sys.executable, step],
            check = True
        )

        logging.info("Completed {step}")


    print("\n==== PIPELINE COMPLETED SUCCESSFULLY ====")
    logging.info("Pipeline completed successfully")

except subprocess.CalledProcessError as error:
    print("\nPIPELINE FAILED!")
    print("Failed script:", error.cmd[-1])

    logging.exception("pipeline execution failed")
    sys.exit(1)

except Exception: 
    print("\nUNEXPECTED ERROR OCCURRED!")

    logging.exception("Unexpected pipeline error")
    sys.exit(1)