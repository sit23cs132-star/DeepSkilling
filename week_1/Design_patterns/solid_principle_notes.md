# SOLID Principles Notes

## Single Responsibility Principle (SRP)
A class should have only one reason to change.  
Example: Separate `InvoicePrinter` from `InvoiceCalculator`.

## Open/Closed Principle (OCP)
Software entities should be open for extension, but closed for modification.  
Example: Adding new payment methods via subclasses without editing existing code.

## Liskov Substitution Principle (LSP)
Objects of a superclass should be replaceable with objects of a subclass without breaking functionality.  
Example: A `Square` class should not violate behavior expected from a `Rectangle`.

## Interface Segregation Principle (ISP)
Clients should not be forced to depend on interfaces they do not use.  
Example: Split `IPrinter` and `IScanner` instead of one bulky interface.

## Dependency Inversion Principle (DIP)
Depend on abstractions, not on concrete implementations.  
Example: Use `PaymentService` interface instead of directly coding to `CreditCardPayment`.
