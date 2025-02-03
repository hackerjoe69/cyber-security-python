import frida
import sys

def on_message(message, data):
    """
    Handles messages sent from the injected Frida script.
    """
    if message['type'] == 'send':
        print(f"[+] {message['payload']}")
    elif message['type'] == 'error':
        print(f"[-] Error: {message['stack']}")

def main(target_app):
    """
    Attaches to an iOS application and performs basic pentesting.
    """
    try:
        print(f"[+] Connecting to the iOS device...")
        device = frida.get_usb_device()
        session = device.attach(target_app)
        print(f"[+] Attached to {target_app}")

        # JavaScript script for hooking Objective-C methods
        script_code = """
        console.log("Injected script into target app.");

        // Example: Hooking a method
        var className = "YourTargetClass"; // Replace with the target class name
        var methodName = "- yourMethod:"; // Replace with the target method name

        var target = ObjC.classes[className][methodName];
        if (target) {
            Interceptor.attach(target.implementation, {
                onEnter: function(args) {
                    console.log("[+] Hooked " + className + "." + methodName);
                    console.log("Argument 0: " + ObjC.Object(args[2]).toString()); // Adjust index based on the method signature
                },
                onLeave: function(retval) {
                    console.log("Return value: " + ObjC.Object(retval).toString());
                }
            });
        } else {
            console.log("[-] Method not found: " + className + "." + methodName);
        }

        // Example: Bypass Jailbreak Detection
        var jbCheck = ObjC.classes.YourTargetClass["- isJailbroken"];
        if (jbCheck) {
            Interceptor.attach(jbCheck.implementation, {
                onLeave: function(retval) {
                    console.log("[+] Bypassing Jailbreak Detection");
                    retval.replace(0x0); // Force return false
                }
            });
        }
        """

        # Load the script into the target process
        script = session.create_script(script_code)
        script.on('message', on_message)
        script.load()

        print("[+] Script injected. Monitoring activity...")
        sys.stdin.read()  # Keep the script running to receive messages

    except frida.ProcessNotFoundError:
        print(f"[-] Could not find the target app: {target_app}")
    except Exception as e:
        print(f"[-] An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ios_pentest.py <bundle_identifier>")
        sys.exit(1)

    target_app = sys.argv[1]
    main(target_app)
