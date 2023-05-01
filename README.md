# faas-wifi-qr

faas function to generate qr code for the wifi given ssid and password.
*auth* arugment can also be passed to define the wifi security WPA/WPA2.

## building and deploying

```faas-cli build -f ./wifi-qr.yaml && faas-cli push -f ./wifi-qr.yaml && faas-cli deploy -f ./wifi-qr.yaml```


> **note**
> [wifi-qr](./wifi-qr.yaml) configuration will have to be adapted.
> I'm using a local registry with ssh , under *registry*
