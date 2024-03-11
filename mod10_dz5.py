from multiprocessing import Process, Manager

class WarehouseManager:
    def __init__(self):
        self.data = Manager().dict()

    def process_request(self, request):
        product, action, quantity = request

        with Manager().Lock():
            if action == "receipt":
                if product in self.data:
                    self.data[product] += quantity
                else:
                    self.data[product] = quantity
            elif action == "shipment":
                if product in self.data and self.data[product] >= quantity:
                    self.data[product] -= quantity

    def process_requests(self, requests):
        processes = [Process(target=self.process_request, args=(request,)) for request in requests]

        for process in processes:
            process.start()
        for process in processes:
            process.join()

    def run(self, requests):
        self.process_requests(requests)

if __name__ == "__main__":
    manager = WarehouseManager()

    requests = [
        ("product1", "receipt", 100),
        ("product2", "receipt", 150),
        ("product1", "shipment", 30),
        ("product3", "receipt", 200),
        ("product2", "shipment", 50)
    ]

    manager.run(requests)
    print(manager.data)