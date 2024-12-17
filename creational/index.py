"""
Creational Patterns

Creational Design Patterns focus on how objects are created. 
They abstract the instantiation process, making your system independent of how its objects are composed and represented. 
These patterns help make a system scalable and flexible by reducing dependencies and ensuring that the right objects are created efficiently.

Types of Creational Patterns:

1. **Factory Method**:
   - Provides a way to delegate the instantiation of objects to subclasses.
   - Defines an interface for creating an object but allows subclasses to alter the type of objects that will be created.
   - **Key Benefits**:
     - Promotes loose coupling between client code and the concrete classes it depends on.
     - Simplifies code maintenance by encapsulating object creation logic.
   - **Use Case**: When a class cannot anticipate the type of objects it needs to create.

2. **Abstract Factory**:
   - Provides an interface for creating families of related or dependent objects without specifying their concrete classes.
   - Encapsulates a group of factories with a common theme, ensuring that related objects are compatible.
   - **Key Benefits**:
     - Helps in creating a consistent look and feel across a family of related objects.
     - Centralizes control of object creation.
   - **Use Case**: When a system needs to create objects that belong to multiple related families.

3. **Builder**:
   - Separates the construction of a complex object from its representation, allowing the same construction process to create different representations.
   - Focuses on constructing objects step-by-step and allows customization at each step.
   - **Key Benefits**:
     - Simplifies the creation of complex objects with multiple configurations.
     - Enhances code readability and reduces the risk of errors in object construction.
   - **Use Case**: When constructing a large or complex object with numerous optional and mandatory attributes.

4. **Prototype**:
   - Creates new objects by cloning an existing object, ensuring a performance boost for costly object creation.
   - Allows an object to be copied and modified without relying on its concrete class.
   - **Key Benefits**:
     - Reduces the overhead of creating complex or resource-intensive objects from scratch.
     - Helps maintain object consistency when duplicating objects with a predefined state.
   - **Use Case**: When the cost of creating an object is high and an existing object can serve as a prototype.

5. **Singleton**:
   - Ensures that a class has only one instance and provides a global point of access to that instance.
   - Restricts instantiation of the class and ensures controlled access to the sole instance.
   - **Key Benefits**:
     - Prevents the creation of multiple instances of a class, saving memory and ensuring consistency.
     - Provides a single point of control for managing shared resources.
   - **Use Case**: When you need a single, shared instance of a class for tasks like logging, configuration, or resource management.

Conclusion:
Creational Patterns provide robust solutions for object creation in software development. 
They promote flexibility and reusability by abstracting the instantiation process and minimizing dependencies. 
By leveraging these patterns, developers can create scalable, maintainable, and efficient systems.
"""
