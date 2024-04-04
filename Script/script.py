from Hermes.Hermes import Hermes as Police

def main(path:str) -> tuple:
    p = Police(path)

    while (p.position != p.map._DEAD_END):
        p.travel_until_curve()
        p.position = p.change_direction()

    return (p.get_amount(), p.get_money_list())


if __name__ == "__main__":
    print(f"[VERBOSE] Initiating Executed!")
    main('./Tests/test-cases/' + 'caseG01.txt')
    print("[VERBOSE] Execution Finished Successfully!")