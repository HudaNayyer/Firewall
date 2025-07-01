import random

def generate_random_ip():
    return f"192.168.1.{random.randint(0,20)}"
#defining the method that generates a random ip number, to represent source ip.

def check_firewall_rules(ip, rules):
    for rule_ip, action in rules.items():
    #for loop to unpack the dictionary via items function for each IPS on blocklist
        if ip == rule_ip:
            return action
        #compare randomly generated IP and see if it matches, and then it "blocks"
    return "allow"
    #allows if it does not match ip on ip blocklist.
#defining the method to check firewall rules that receives IP and rules as an argument
        
    
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
        print(f"TP: {ip_address}, Action:{action}, Random: {random_number}")
        #print ip address of the packet analyzed, the action taken against ip, and random unique iditenifier number
    
    if __name__ == "__main__":
        main()
