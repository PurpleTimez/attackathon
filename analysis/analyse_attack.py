import subprocess
import attacker_cost

lncli_commands = [
    "kubectl exec -it flagship -n warnet-armada -- lncli --network=regtest --tlscertpath=/credentials/lnd0-tls.cert --macaroonpath=/credentials/lnd0-admin.macaroon --rpcserver=lightning-0.warnet-armada",
    "kubectl exec -it flagship -n warnet-armada -- lncli --network=regtest --tlscertpath=/credentials/lnd1-tls.cert --macaroonpath=/credentials/lnd1-admin.macaroon --rpcserver=lightning-1.warnet-armada",
    "kubectl exec -it flagship -n warnet-armada -- lncli --network=regtest --tlscertpath=/credentials/lnd2-tls.cert --macaroonpath=/credentials/lnd2-admin.macaroon --rpcserver=lightning-2.warnet-armada"
]

if __name__ == "__main__":
    results = {}
    total_payment_count = 0
    total_success = 0
    total_upfront = 0

    for i, command in enumerate(lncli_commands):
        results[f'lncli{i}'] = attacker_cost.main(command)
        total_payment_count += results[f'lncli{i}']['payment_count']
        total_success += results[f'lncli{i}']['success']
        total_upfront += results[f'lncli{i}']['upfront']

    print(f"Attacker sent: {total_payment_count} payments paying {total_success+total_upfront} msat fees\n")

    for key, value in results.items():
        print(f"{key}: {value}")
