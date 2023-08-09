# Interface for processing payments
class PaymentProcessor:
    def process_payment(self, amount):
        print(f"Processing payment of ${amount}")

# Interface for processing refunds
class RefundProcessor:
    def process_refund(self, amount):
        print(f"Processing refund of ${amount}")

# Class for handling payment processing
class OnlinePaymentProcessor(PaymentProcessor):
    def process_payment(self, amount):
        super().process_payment(amount)

# Class for handling both payment and refund processing
class OnlinePaymentRefundProcessor(PaymentProcessor, RefundProcessor):
    def process_payment(self, amount):
        super().process_payment(amount)

    def process_refund(self, amount):
        super().process_refund(amount)


if __name__ == "__main__":
    # Simulate payment processing using OnlinePaymentProcessor
    payment_processor = OnlinePaymentProcessor()
    payment_processor.process_payment(900)

    # Simulate refund processing using OnlinePaymentRefundProcessor
    refund_processor = OnlinePaymentRefundProcessor()
    refund_processor.process_refund(90)
