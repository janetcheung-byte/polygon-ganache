import subprocess
import os
import argparse


# Current Dir
workdir = os.getcwd()


class PolygonController:
    
    global workdir

    @staticmethod
    def truffle_unbox():

        cmd = "truffle unbox polygon"

        print("running truffle unbox")

        process = subprocess.call(cmd, shell=True)
        return process

    
    @staticmethod
    def place_contract():
        curr_dir = workdir
        cmd = "ls"

        process = subprocess.call(cmd,shell=True)
        return process




    @staticmethod
    def compile_poly():
        cmd = "npm run compile:polygon"

        process = subprocess.call(cmd,shell=True)

        return process


    @staticmethod
    def migrate():
        cmd = "npm run migrate:polygon"
        process = subprocess.call(cmd,shell=True)

        return process



if __name__ == "__main__":
    # PolygonController().truffle_unbox()
    PolygonController().place_contract()
    # PolygonController().compile_poly()
    # PolygonController().migrate()

