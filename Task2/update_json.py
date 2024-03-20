import json

def update(initial_meta, command, namespace, values, type=1):
    if command == 'append':
        not_exist = True
        new_item = {
            "Name": namespace,
            "Type": type,
            "Value": values
        }

        # Checking the existence of item in json
        for item in initial_meta:
            if item.get('Name') == namespace:
                not_exist = False
                print(f"Item '{namespace}' already exists. Cannot append.")
                break

        # Checking the previous item name number existence
        if not_exist:
            if namespace.split("::")[-1].isdigit():
                current_number = int(namespace.split("::")[-1])
                previous_namespace = "::".join(namespace.split("::")[:-1]) + f"::{current_number - 1}"
                if any(item.get('Name') == previous_namespace for item in initial_meta):
                    initial_meta.append(new_item)
                    print(f"Item '{namespace}' added.")
                else:
                    print(f"Previous item '{previous_namespace}' doesn't exist. Cannot append.")
            else:
                initial_meta.append(new_item)
                print(f"Item '{namespace}' added.")

    # Checking the existence of item in json for deletion
    if command == 'delete':
        item_found = False
        for item in initial_meta:
            if item.get("Name") == namespace:
                initial_meta.remove(item)
                print(f"Item '{namespace}' deleted.")
                item_found = True
                break
        if not item_found:
            print(f"Item '{namespace}' doesn't exist. Cannot delete.")

    return initial_meta

with open("venv/Scripts/Task2/game_build.json", "r") as file:
    meta = json.load(file)

meta_new = update(meta, "append", "GTL::Build::Tags", ["DX13", "Uplay", "DLSS"], 1)
meta_new = update(meta_new, "delete", "GTL::Build::Categories", "NODRM")

# Write the updated meta info back to the same JSON file
with open("venv/Scripts/Task2/game_build.json", "w") as file:
    json.dump(meta_new, file, indent=4)
