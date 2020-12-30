# Instances in [[202012211226 Swift Programming Language|Swift]]

[[202012211429 Object Types - Swift|Object types]] have an important feature in common: they can be **instantiated**. 

## Definition

When you declare an object type, you are only defining a *type*. To instantiate a type is to make a thing - an instance - of that type.

## Example

We can declare a dog type of object in the following manner: 

```Swift
class Dog {
	func bark() {
		print("woof")
	}
	var name = ""
}
```

However, in the above segment, we do not have a dog object. What do have is a type. It shows what a `Dog` object would be like if we have one. To make a `Dog` instance, we need to: 

```Swift
let fido = Dog()
```

Not the parentheses here. ==We append parentheses to the name of an object type to send a message to that object type, asking it to instantiate itself.==

Now, after we have instantiated a `Dog` instance, we are able to call its [[202012211454 Property - Swift|properties]] and [[202012211455 Method - Swift|methods]]:

```Swift
fido.name = "Fido"
fido.bark() // output: woof
```

## Important Note

By default, [[202012211454 Property - Swift|properties]] and [[202012211455 Method - Swift|methods]] are *instance* properties and methods, meaning that you **CANNOT** use them as messages to the object type itself. You have to have an instance to send those messages to.

```Swift
Dog.bark() // compile error
```

It is possible to declare a function bark in such a way that saying `Dog.bark()` is legal, but that would be a **different** kind of function: ==a class function or a static function==, and you would need to say so when you declare it. 

## Why Instances?

Given that an [[202012211429 Object Types - Swift|object type]] itself is an object, why do we need instances?
- We use [[202012211429 Object Types - Swift|object types]] to define the type of objects, and then we could instantiate different objects that conform to that specific object type. 
- We could have an [[202012211429 Object Types - Swift|object type]] `Dog`, and then we could have different objects that are typed `Dog`, such as `dog1`, `dog2`, `Michael`...

**Essentially,** an instance is ==both code and data==. The code is from its type and shared with other instances of the same type, but the data is of its own.