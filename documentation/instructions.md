# Instructions

Download the source code of the [latest release](https://github.com/ni-eminen/ReactComponentViewer/releases).

## Configuring

There is no need for configuring for the user. A local database file is created and initialized with a schema automatically

## Running the program

Install dependencies:

```bash
poetry install
```

Run the program via:

```
poetry run invoke start
```

## Logging in

The program will prompt you to sign in or to create a new account:

![](https://github.com/ni-eminen/ReactComponentViewer/blob/main/documentation/imgs/login_screen.png)

You can create a new account and login by typing out the desired username and password and pressing on `Create account` followed by `Login`.

## Creating a component

After logging on you will land on the create component screen. You can input your own component or render the example by clicking on `Render component`. 

![](https://github.com/ni-eminen/ReactComponentViewer/blob/main/documentation/imgs/add_component_screen.png)

You can save a new component by clicking on `Save component` and typing out the desired name for the new component and clicking OK.

![](https://github.com/ni-eminen/ReactComponentViewer/blob/main/documentation/imgs/saving_component.png)

## Viewing components

You can navigate to the components screen by clicking on the buttons on the sidebar.

![](https://github.com/ni-eminen/ReactComponentViewer/blob/main/documentation/imgs/components_screen.png)

## Editing components

You can edit a selected component by clicking save changes after making changes to the text on the Components screen.

## Deleting components

You can delete a selected component by clicking on `Delete component`.

## Viewing community components

Community components are all components that have been saved by any user whereas user components are your own components.

You can display community components by clicking on the `Community` button located on the top of the components list. Similarly, you can switch back to your own components by clicking on `User`.
