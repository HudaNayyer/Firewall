import random


def main():
    firewall_rules = {
        #ip addresses not allowed on internal network
        "192.168.1.1": "block",
        "192.168.1.4": "block",
        "192.168.1.9": "block",
        "192.168.1.13": "block",
        "192.168.1.16": "block",
        "192.168.1.19": "block",
    }

    for _ in range(12):
    #for loop that runs 12 times to simulate netowrk traffic
        ip_address = generate_random_ip()
        #variable ip address to assign the calue returned by generate_random_ip() function
        action = check_firewall_rules(ip_address, firewall_rules)
        #variable action that assings the value returned by the function to check firewall rules
        random_number = random.randint(0,9999)
        #random variable between 0 - 9999 too serve as a unique identifier for when we
        # take multiple actions against a single IP, we have an distinguisher between those actions
        print()
    
    if __name__ == "__main__":
        main()
