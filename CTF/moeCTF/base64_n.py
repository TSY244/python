import base64


def decodeBase64_n(strs):
    answer = strs
    while True:
        try:
            answer = base64.decodebytes(answer.encode("utf-8"))
            answer = answer.decode("utf-8")
            print(answer)
        except Exception as e:
            print(f"结果是：{answer}")
            break


def encryption_n(strs, n):
    answer = strs

    for i in range(n):
        decode_bytes = base64.decodebytes(answer.encode("utf-8"))
        answer = decode_bytes.decode("utf-8")
    print(f"一共加密了{n}次，结果是{answer}")


encryption_n("eyJ1c2VybmFtZSI6IjEyIiwicGFzc3dvcmQiOiIxMjMifQ==", 4)
# decodeBase64_n("VjJ4b2MxTXdNVmhVV0d4WFltMTRjRmxzVm1GTlJtUnpWR3R3VDJFeWVIaFZiR2h6VTIxR1dWcElRbHBOUjFKSVdsY3hUbVZzY0VsWGJYQnBWbXRhZDFaRVNuTlRiVlpHVFZoR1ZWWXllSFJXVmxGM1QxRTlQUT09")
