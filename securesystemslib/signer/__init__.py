"""
The Signer API

This module provides extensible interfaces for public keys and signers:
Some implementations are provided by default but more can be added by users.
"""
from securesystemslib.signer._azure_signer import AzureSigner
from securesystemslib.signer._gcp_signer import GCPSigner
from securesystemslib.signer._gpg_signer import GPGKey, GPGSigner
from securesystemslib.signer._hsm_signer import HSMSigner
from securesystemslib.signer._key import KEY_FOR_TYPE_AND_SCHEME, Key, SSlibKey
from securesystemslib.signer._signature import Signature
from securesystemslib.signer._signer import (
    SIGNER_FOR_URI_SCHEME,
    SecretsHandler,
    Signer,
    SSlibSigner,
)
from securesystemslib.signer._sigstore_signer import SigstoreKey, SigstoreSigner
from securesystemslib.signer._spx_signer import (
    SpxKey,
    SpxSigner,
    generate_spx_key_pair,
)

# Register supported private key uri schemes and the Signers implementing them
SIGNER_FOR_URI_SCHEME.update(
    {
        SSlibSigner.ENVVAR_URI_SCHEME: SSlibSigner,
        SSlibSigner.FILE_URI_SCHEME: SSlibSigner,
        GCPSigner.SCHEME: GCPSigner,
        HSMSigner.SCHEME: HSMSigner,
        GPGSigner.SCHEME: GPGSigner,
        AzureSigner.SCHEME: AzureSigner,
    }
)

# Register supported key types and schemes, and the Keys implementing them
KEY_FOR_TYPE_AND_SCHEME.update(
    {
        ("ecdsa", "ecdsa-sha2-nistp256"): SSlibKey,
        ("ecdsa", "ecdsa-sha2-nistp384"): SSlibKey,
        ("ecdsa-sha2-nistp256", "ecdsa-sha2-nistp256"): SSlibKey,
        ("ecdsa-sha2-nistp384", "ecdsa-sha2-nistp384"): SSlibKey,
        ("ed25519", "ed25519"): SSlibKey,
        ("rsa", "rsassa-pss-sha224"): SSlibKey,
        ("rsa", "rsassa-pss-sha256"): SSlibKey,
        ("rsa", "rsassa-pss-sha384"): SSlibKey,
        ("rsa", "rsassa-pss-sha512"): SSlibKey,
        ("rsa", "rsa-pkcs1v15-sha224"): SSlibKey,
        ("rsa", "rsa-pkcs1v15-sha256"): SSlibKey,
        ("rsa", "rsa-pkcs1v15-sha384"): SSlibKey,
        ("rsa", "rsa-pkcs1v15-sha512"): SSlibKey,
        ("sphincs", "sphincs-shake-128s"): SpxKey,
        ("rsa", "pgp+rsa-pkcsv1.5"): GPGKey,
        ("dsa", "pgp+dsa-fips-180-2"): GPGKey,
        ("eddsa", "pgp+eddsa-ed25519"): GPGKey,
    }
)
