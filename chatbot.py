# Copyright (c) Lineaje, Inc. All rights reserved.
# Lineaje UnifAI guardrail  version=2.0.0-alpha
def _lineaje_load_gr_client():
    """Lineaje-added: load gr_stub_client.py without a pip dependency."""
    import sys as _s, importlib.util as _ilu
    from pathlib import Path as _P
    n = "_lineaje_gr_stub_client"
    if n in _s.modules: return _s.modules[n]
    h = _P(__file__).resolve().parent
    _cand = next((d / "gr_stub_client.py" for d in [h, *h.parents][:8] if (d / "gr_stub_client.py").is_file()), h / "gr_stub_client.py")
    _spec = _ilu.spec_from_file_location(n, _cand)
    _s.modules[n] = _m = _ilu.module_from_spec(_spec)
    _spec.loader.exec_module(_m); return _m
def _lineaje_current_model():
    """Lineaje-added: reread the app's model setting for every request."""
    import os as _o
    from pathlib import Path as _P
    _keys = ("OPENROUTER_MODEL", "LLM_MODEL", "MODEL_NAME", "MODEL_ID", "OPENAI_MODEL", "ANTHROPIC_MODEL", "BEDROCK_MODEL_ID")
    _here = _P(__file__).resolve().parent
    for _path in (_here / ".env", *(_p / ".env" for _p in list(_here.parents)[:8])):
        if not _path.is_file(): continue
        try: _lines = _path.read_text(encoding="utf-8").splitlines()
        except OSError: continue
        _values = {}
        for _line in _lines:
            _line = _line.strip()
            if not _line or _line.startswith("#") or "=" not in _line: continue
            _key, _, _value = _line.partition("=")
            if _key.strip() in _keys: _values[_key.strip()] = _value.strip().strip(chr(34)).strip(chr(39))
        for _key in _keys:
            if _values.get(_key): return _values[_key]
    return next((_o.environ[_key].strip() for _key in _keys if _o.environ.get(_key, "").strip()), "")

import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Create client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

# Store conversation
messages = [
    {"role": "system", "content": "You are a helpful assistant."}
]

_lineaje_payload = "AI Chatbot started! Type 'quit' to stop."
# LINEAJE: enforce() `_lineaje_payload` at agent->log log_emit — scan flagged AI_DAT_SEC_012 (Mask PII on user interfaces). Mask/block; do not remove without review. site_id='site:sha256:ed624d7387b012c7fb9cd362810981cf06f0368728f7f1f39af7a066293107f4'
_gr_client = _lineaje_load_gr_client()
_gr_site = _gr_client.SiteDescriptor(site_id='site:sha256:ed624d7387b012c7fb9cd362810981cf06f0368728f7f1f39af7a066293107f4', phase='log_emit', boundary={'source': 'log', 'sink': 'log'}, candidate_policies=[{'policy_id': 'AI_AGENT_ACTIVITY_LOG', 'policy_name': 'Emit Agent Activity via OpenTelemetry', 'guardrail_id': None, 'policy_version': None}], fail_mode='ALLOW_WITH_AUDIT', source_type='agent', destination_type='log', project='lineaje-openclaw', organization='Enterprise', project_name='ai-chatbot', project_version='main', project_branch='main', components={'source': {'entity_type': 'agent', 'unique_org_id': 'vdna_1bOIDPqj97q6mzc6', 'repository_uri': 'https://github.com/abhijnya002/ai-chatbot', 'file_path': 'chatbot.py', 'line': 31, 'name': 'chatbot'}, 'identity': {'source': {'entity_type': 'aiagent', 'name': 'chatbot', 'version': '1.0.0', 'purl': 'pkg:aiagent/chatbot@1.0.0'}, 'app': {'name': 'ai-chatbot', 'version': 'main', 'purl': 'pkg:github/abhijnya002/ai-chatbot@main?commit-id=7cda29133ef56e84a0eede9c324ae7604c776dfe&commit-time=&build_file=requirements.txt&repo_strategy=single-repo'}}, 'invocation': {'file': 'chatbot.py', 'line': 19, 'function': ''}})
try:
    _lineaje_payload = _gr_client.enforce(_gr_site, _lineaje_payload, content_type='application/json')
except _gr_client.GuardrailUnavailableError:
    pass
except PermissionError:
    pass
print(_lineaje_payload)

while True:
    try:
        _lineaje_obs = _lineaje_load_gr_client()
        _lineaje_obs_site = _lineaje_obs.SiteDescriptor(site_id='site:sha256:aa2c05f4de00fea08211b1b3edd364e20e3fa266c93401f1b2df1fabc207fbcb', phase='', boundary={}, candidate_policies=['AI_AGENT_ACTIVITY_LOG'], fail_mode='ALLOW', source_type='user_interface', destination_type='agent', project='lineaje-openclaw', organization='', components={'file': 'chatbot.py', 'line': 22, 'call_target': 'input'}, observe_only=True)
        _lineaje_obs.enforce(_lineaje_obs_site, {'activity': 'ui_to_agent'}, content_type='application/json')
    except Exception:
        pass
    user_input = input("You: ")

    if user_input.lower() in ["quit", "exit"]:
        _lineaje_payload = "Chat ended."
        # LINEAJE: enforce() `_lineaje_payload` at agent->log log_emit — scan flagged AI_DAT_SEC_012 (Mask PII on user interfaces). Mask/block; do not remove without review. site_id='site:sha256:a72da41e95204bc39209257371f9946776a0d2d29d96eceeee50efe86e3909c4'
        _gr_client = _lineaje_load_gr_client()
        _gr_site = _gr_client.SiteDescriptor(site_id='site:sha256:a72da41e95204bc39209257371f9946776a0d2d29d96eceeee50efe86e3909c4', phase='log_emit', boundary={'source': 'log', 'sink': 'log'}, candidate_policies=[{'policy_id': 'AI_AGENT_ACTIVITY_LOG', 'policy_name': 'Emit Agent Activity via OpenTelemetry', 'guardrail_id': None, 'policy_version': None}], fail_mode='ALLOW_WITH_AUDIT', source_type='agent', destination_type='log', project='lineaje-openclaw', organization='Enterprise', project_name='ai-chatbot', project_version='main', project_branch='main', components={'source': {'entity_type': 'agent', 'unique_org_id': 'vdna_1bOIDPqj97q6mzc6', 'repository_uri': 'https://github.com/abhijnya002/ai-chatbot', 'file_path': 'chatbot.py', 'line': 31, 'name': 'chatbot'}, 'identity': {'source': {'entity_type': 'aiagent', 'name': 'chatbot', 'version': '1.0.0', 'purl': 'pkg:aiagent/chatbot@1.0.0'}, 'app': {'name': 'ai-chatbot', 'version': 'main', 'purl': 'pkg:github/abhijnya002/ai-chatbot@main?commit-id=7cda29133ef56e84a0eede9c324ae7604c776dfe&commit-time=&build_file=requirements.txt&repo_strategy=single-repo'}}, 'invocation': {'file': 'chatbot.py', 'line': 25, 'function': ''}})
        try:
            _lineaje_payload = _gr_client.enforce(_gr_site, _lineaje_payload, content_type='application/json')
        except _gr_client.GuardrailUnavailableError:
            pass
        except PermissionError:
            pass
        print(_lineaje_payload)
        break

    _lineaje_payload = {"role": "user", "content": user_input}
    # LINEAJE: enforce() `_lineaje_payload` at agent->llm pre_model — scan flagged AI_APP_SEC_070 (Detect and block all forms of prompt injection attacks in user inputs and file contents). Mask/block; do not remove without review. site_id='site:sha256:8c1e1a31dedf198fc0165d138b43fab7cd7d5d032454fa0d853b75547b41536b'
    _gr_client = _lineaje_load_gr_client()
    _gr_site = _gr_client.SiteDescriptor(site_id='site:sha256:8c1e1a31dedf198fc0165d138b43fab7cd7d5d032454fa0d853b75547b41536b', phase='pre_model', boundary={'source': 'agent_message', 'sink': 'model'}, candidate_policies=[{'policy_id': 'AI_APP_SEC_006', 'policy_name': "Use only LLMs from the organization's approved list.", 'guardrail_id': 'Enforce Approved LLM.', 'policy_version': '2026.08.1'}, {'policy_id': 'AI_APP_SEC_038', 'policy_name': 'The AI Model must validate and sanitize any input before processing.', 'guardrail_id': 'Sanitize LLM Input', 'policy_version': '2026.08.1'}, {'policy_id': 'AI_APP_SEC_067', 'policy_name': 'Detect direct string interpolation of untrusted input into LLM prompts', 'guardrail_id': 'Enforce structural separation of untrusted input from LLM prompt templates', 'policy_version': '2026.08.1'}, {'policy_id': 'AI_APP_SEC_001', 'policy_name': 'Do not allow malicious content via hidden prompts', 'guardrail_id': 'Replace suspicious prompt', 'policy_version': '2026.08.1'}, {'policy_id': 'AI_APP_SEC_039', 'policy_name': 'Sanitize and validate all input to the AI Model.', 'guardrail_id': 'Sanitize LLM input', 'policy_version': '2026.08.1'}, {'policy_id': 'AI_APP_SEC_080', 'policy_name': 'Do not allow refusal-triggering language in LLM driven analysis pipeline', 'guardrail_id': 'Replace refusal-triggering language in untrusted content', 'policy_version': '2026.08.1'}, {'policy_id': 'AI_APP_SEC_032', 'policy_name': 'Do not allow malicious content via hidden prompts written in leetspeak.', 'guardrail_id': 'Remove prompts in leetspeak', 'policy_version': '2026.08.1'}, {'policy_id': 'AI_APP_SEC_059', 'policy_name': 'Do not allow prompts that can execute malicious commands at runtime.', 'guardrail_id': 'Block runtime command execution prompts.', 'policy_version': '2026.08.1'}, {'policy_id': 'AI_APP_SEC_028', 'policy_name': "Do not use LLMs from the organization's disallowed list", 'guardrail_id': 'Enforce Approved LLM', 'policy_version': '2026.08.1'}, {'policy_id': 'AI_APP_SEC_002', 'policy_name': 'Do not allow malicious content via encoded prompts', 'guardrail_id': 'Replace suspicious prompt.', 'policy_version': '2026.08.1'}, {'policy_id': 'AI_APP_SEC_070', 'policy_name': 'Detect and block all forms of prompt injection attacks in user inputs and file contents', 'guardrail_id': 'Neutralize all detected prompt injection payloads', 'policy_version': '2026.08.1'}, {'policy_id': 'AI_DAT_SEC_011', 'policy_name': 'Do not send PII and/or secrets to AI Models', 'guardrail_id': 'Redact PII', 'policy_version': '2026.08.1'}, {'policy_id': 'AI_APP_SEC_071', 'policy_name': 'Enforce chemical, biological, radiological, or nuclear (CBRN) threat prevention safeguards in AI-enabled systems', 'guardrail_id': 'Add CBRN screening and biological data safeguards.', 'policy_version': '2026.08.1'}, {'policy_id': 'AI_AGENT_ACTIVITY_LOG', 'policy_name': 'AI agent activity must be logged via OpenTelemetry.', 'guardrail_id': 'Emit Agent Activity via OpenTelemetry (single prompt)', 'policy_version': '2026.08.1'}], fail_mode='BLOCK', source_type='agent', destination_type='llm', project='lineaje-openclaw', organization='Enterprise', project_name='ai-chatbot', project_version='main', project_branch='main', components={'source': {'entity_type': 'agent', 'unique_org_id': 'vdna_1bOIDPqj97q6mzc6', 'repository_uri': 'https://github.com/abhijnya002/ai-chatbot', 'file_path': 'chatbot.py', 'line': 31, 'name': 'chatbot'}, 'destination': {'entity_type': 'llm', 'name': 'nemotron-3-super-120b-a12b:free', 'version': '', 'provider': 'nvidia'}, 'identity': {'source': {'entity_type': 'aiagent', 'name': 'chatbot', 'version': '1.0.0', 'purl': 'pkg:aiagent/chatbot@1.0.0'}, 'app': {'name': 'ai-chatbot', 'version': 'main', 'purl': 'pkg:github/abhijnya002/ai-chatbot@main?commit-id=7cda29133ef56e84a0eede9c324ae7604c776dfe&commit-time=&build_file=requirements.txt&repo_strategy=single-repo'}, 'destination': {'entity_type': 'aimodel', 'name': 'NVIDIA', 'version': 'nemotron-3-super-120b-a12b:free', 'purl': 'pkg:aimodel/NVIDIA@nemotron-3-super-120b-a12b:free'}}, 'invocation': {'file': 'chatbot.py', 'line': 28, 'function': ''}})
    try:
        _lineaje_payload = _gr_client.enforce(_gr_site, _lineaje_payload, content_type='application/json', variable_name='_lineaje_payload', source_file=__file__, before_line=28)
    except _gr_client.GuardrailUnavailableError:
        pass
    except PermissionError:
        raise
    messages.append(_lineaje_payload)

    try:
        # LINEAJE: enforce() `messages` at agent->llm pre_model — scan flagged AI_APP_SEC_070 (Detect and block all forms of prompt injection attacks in user inputs and file contents); AI_DAT_SEC_012 (Mask PII on user interfaces). Mask/block; do not remove without review. site_id='site:sha256:70fa495cc0463b8b62feb916383129fae87c701c8f49a86dcbe658cfd682c629'
        _lineaje_messages_evidence = {'messages': messages, 'model': 'nvidia/nemotron-3-super-120b-a12b:free', 'project': 'lineaje-openclaw'}
        _gr_client = _lineaje_load_gr_client()
        _gr_site = _gr_client.SiteDescriptor(site_id='site:sha256:70fa495cc0463b8b62feb916383129fae87c701c8f49a86dcbe658cfd682c629', phase='pre_model', boundary={'source': 'agent_message', 'sink': 'model'}, candidate_policies=[{'policy_id': 'AI_APP_SEC_006', 'policy_name': "Use only LLMs from the organization's approved list.", 'guardrail_id': 'Enforce Approved LLM.', 'policy_version': '2026.08.1'}, {'policy_id': 'AI_APP_SEC_038', 'policy_name': 'The AI Model must validate and sanitize any input before processing.', 'guardrail_id': 'Sanitize LLM Input', 'policy_version': '2026.08.1'}, {'policy_id': 'AI_APP_SEC_067', 'policy_name': 'Detect direct string interpolation of untrusted input into LLM prompts', 'guardrail_id': 'Enforce structural separation of untrusted input from LLM prompt templates', 'policy_version': '2026.08.1'}, {'policy_id': 'AI_APP_SEC_001', 'policy_name': 'Do not allow malicious content via hidden prompts', 'guardrail_id': 'Replace suspicious prompt', 'policy_version': '2026.08.1'}, {'policy_id': 'AI_APP_SEC_039', 'policy_name': 'Sanitize and validate all input to the AI Model.', 'guardrail_id': 'Sanitize LLM input', 'policy_version': '2026.08.1'}, {'policy_id': 'AI_APP_SEC_080', 'policy_name': 'Do not allow refusal-triggering language in LLM driven analysis pipeline', 'guardrail_id': 'Replace refusal-triggering language in untrusted content', 'policy_version': '2026.08.1'}, {'policy_id': 'AI_APP_SEC_032', 'policy_name': 'Do not allow malicious content via hidden prompts written in leetspeak.', 'guardrail_id': 'Remove prompts in leetspeak', 'policy_version': '2026.08.1'}, {'policy_id': 'AI_APP_SEC_059', 'policy_name': 'Do not allow prompts that can execute malicious commands at runtime.', 'guardrail_id': 'Block runtime command execution prompts.', 'policy_version': '2026.08.1'}, {'policy_id': 'AI_APP_SEC_028', 'policy_name': "Do not use LLMs from the organization's disallowed list", 'guardrail_id': 'Enforce Approved LLM', 'policy_version': '2026.08.1'}, {'policy_id': 'AI_APP_SEC_002', 'policy_name': 'Do not allow malicious content via encoded prompts', 'guardrail_id': 'Replace suspicious prompt.', 'policy_version': '2026.08.1'}, {'policy_id': 'AI_APP_SEC_070', 'policy_name': 'Detect and block all forms of prompt injection attacks in user inputs and file contents', 'guardrail_id': 'Neutralize all detected prompt injection payloads', 'policy_version': '2026.08.1'}, {'policy_id': 'AI_DAT_SEC_011', 'policy_name': 'Do not send PII and/or secrets to AI Models', 'guardrail_id': 'Redact PII', 'policy_version': '2026.08.1'}, {'policy_id': 'AI_APP_SEC_071', 'policy_name': 'Enforce chemical, biological, radiological, or nuclear (CBRN) threat prevention safeguards in AI-enabled systems', 'guardrail_id': 'Add CBRN screening and biological data safeguards.', 'policy_version': '2026.08.1'}, {'policy_id': 'AI_AGENT_ACTIVITY_LOG', 'policy_name': 'AI agent activity must be logged via OpenTelemetry.', 'guardrail_id': 'Emit Agent Activity via OpenTelemetry (single prompt)', 'policy_version': '2026.08.1'}], fail_mode='BLOCK', source_type='agent', destination_type='llm', project='lineaje-openclaw', organization='Enterprise', project_name='ai-chatbot', project_version='main', project_branch='main', components={'source': {'entity_type': 'agent', 'unique_org_id': 'vdna_1bOIDPqj97q6mzc6', 'repository_uri': 'https://github.com/abhijnya002/ai-chatbot', 'file_path': 'chatbot.py', 'line': 31, 'name': 'chatbot'}, 'destination': {'entity_type': 'llm', 'name': 'nemotron-3-super-120b-a12b:free', 'version': '', 'provider': 'nvidia'}, 'identity': {'source': {'entity_type': 'aiagent', 'name': 'chatbot', 'version': '1.0.0', 'purl': 'pkg:aiagent/chatbot@1.0.0'}, 'app': {'name': 'ai-chatbot', 'version': 'main', 'purl': 'pkg:github/abhijnya002/ai-chatbot@main?commit-id=7cda29133ef56e84a0eede9c324ae7604c776dfe&commit-time=&build_file=requirements.txt&repo_strategy=single-repo'}, 'destination': {'entity_type': 'aimodel', 'name': 'NVIDIA', 'version': 'nemotron-3-super-120b-a12b:free', 'purl': 'pkg:aimodel/NVIDIA@nemotron-3-super-120b-a12b:free'}}, 'invocation': {'file': 'chatbot.py', 'line': 31, 'function': ''}})
        try:
            _lineaje_messages_evidence = _gr_client.enforce(_gr_site, _lineaje_messages_evidence, content_type='application/json')
            messages = _lineaje_messages_evidence.get('messages', messages) if isinstance(_lineaje_messages_evidence, dict) else messages
        except _gr_client.GuardrailUnavailableError:
            pass
        except PermissionError:
            raise
        response = client.chat.completions.create(
            model="nvidia/nemotron-3-super-120b-a12b:free",
            messages=messages
        )

        reply = response.choices[0].message.content
        # LINEAJE: enforce() `reply` at llm->agent post_model — scan flagged AI_DAT_SEC_012 (Mask PII on user interfaces). Mask/block; do not remove without review. site_id='site:sha256:55171778fd7c3720ec8dd579051eab96945d861c81a1eef12fc5071179f7dd80'
        _gr_client = _lineaje_load_gr_client()
        _gr_site = _gr_client.SiteDescriptor(site_id='site:sha256:55171778fd7c3720ec8dd579051eab96945d861c81a1eef12fc5071179f7dd80', phase='post_model', boundary={'source': 'model', 'sink': 'agent_message'}, candidate_policies=[{'policy_id': 'AI_DAT_SEC_029', 'policy_name': 'Enforce decision logging, audit trail, and forensic readiness for AI-driven actions.', 'guardrail_id': 'Emit immutable, forensic-ready audit records for all AI decisions.', 'policy_version': '2026.08.1'}, {'policy_id': 'AI_AGENT_ACTIVITY_LOG', 'policy_name': 'AI agent activity must be logged via OpenTelemetry.', 'guardrail_id': 'Emit Agent Activity via OpenTelemetry (single prompt)', 'policy_version': '2026.08.1'}], fail_mode='BLOCK', source_type='llm', destination_type='agent', project='lineaje-openclaw', organization='Enterprise', project_name='ai-chatbot', project_version='main', project_branch='main', components={'source': {'entity_type': 'agent', 'unique_org_id': 'vdna_1bOIDPqj97q6mzc6', 'repository_uri': 'https://github.com/abhijnya002/ai-chatbot', 'file_path': 'chatbot.py', 'line': 31, 'name': 'chatbot'}, 'destination': {'entity_type': 'llm', 'name': 'nemotron-3-super-120b-a12b:free', 'version': '', 'provider': 'nvidia'}, 'identity': {'source': {'entity_type': 'aiagent', 'name': 'chatbot', 'version': '1.0.0', 'purl': 'pkg:aiagent/chatbot@1.0.0'}, 'app': {'name': 'ai-chatbot', 'version': 'main', 'purl': 'pkg:github/abhijnya002/ai-chatbot@main?commit-id=7cda29133ef56e84a0eede9c324ae7604c776dfe&commit-time=&build_file=requirements.txt&repo_strategy=single-repo'}, 'destination': {'entity_type': 'aimodel', 'name': 'NVIDIA', 'version': 'nemotron-3-super-120b-a12b:free', 'purl': 'pkg:aimodel/NVIDIA@nemotron-3-super-120b-a12b:free'}}, 'invocation': {'file': 'chatbot.py', 'line': 36, 'function': ''}})
        try:
            reply = _gr_client.enforce(_gr_site, reply, content_type='application/json', variable_name='reply', source_file=__file__, before_line=36)
        except _gr_client.GuardrailUnavailableError:
            pass
        # LINEAJE: enforce() `reply` at agent->user_interface data_egress — scan flagged AI_DAT_SEC_012 (Mask PII on user interfaces). Mask/block; do not remove without review. site_id='site:sha256:70b32f5c54755424dc980b884c0079e6b4b1410808cb884b4bce8fb3b09abdc6'
        _gr_client = _lineaje_load_gr_client()
        _gr_site = _gr_client.SiteDescriptor(site_id='site:sha256:70b32f5c54755424dc980b884c0079e6b4b1410808cb884b4bce8fb3b09abdc6', phase='data_egress', boundary={'source': 'agent_message', 'sink': 'user_interface'}, candidate_policies=[{'policy_id': 'AI_DAT_SEC_012', 'policy_name': 'Mask PII on user interfaces', 'guardrail_id': 'Mask PII on UI', 'policy_version': '2026.08.1'}, {'policy_id': 'AI_AGENT_ACTIVITY_LOG', 'policy_name': 'Emit Agent Activity via OpenTelemetry', 'guardrail_id': None, 'policy_version': None}], fail_mode='BLOCK', source_type='agent', destination_type='user_interface', project='lineaje-openclaw', organization='Enterprise', project_name='ai-chatbot', project_version='main', project_branch='main', components={'source': {'entity_type': 'agent', 'unique_org_id': 'vdna_1bOIDPqj97q6mzc6', 'repository_uri': 'https://github.com/abhijnya002/ai-chatbot', 'file_path': 'chatbot.py', 'line': 31, 'name': 'chatbot'}, 'identity': {'source': {'entity_type': 'aiagent', 'name': 'chatbot', 'version': '1.0.0', 'purl': 'pkg:aiagent/chatbot@1.0.0'}, 'app': {'name': 'ai-chatbot', 'version': 'main', 'purl': 'pkg:github/abhijnya002/ai-chatbot@main?commit-id=7cda29133ef56e84a0eede9c324ae7604c776dfe&commit-time=&build_file=requirements.txt&repo_strategy=single-repo'}}, 'invocation': {'file': 'chatbot.py', 'line': 36, 'function': ''}})
        try:
            reply = _gr_client.enforce(_gr_site, reply, content_type='text/plain')
        except _gr_client.GuardrailUnavailableError:
            pass
        except PermissionError:
            pass
        # LINEAJE: enforce() `reply` at agent->log log_emit — scan flagged AI_DAT_SEC_012 (Mask PII on user interfaces). Mask/block; do not remove without review. site_id='site:sha256:c8efd315656a0577efbfe1b45dc1925e8cf5ceca6b851a1393803b5823a0e2cf'
        _gr_client = _lineaje_load_gr_client()
        _gr_site = _gr_client.SiteDescriptor(site_id='site:sha256:c8efd315656a0577efbfe1b45dc1925e8cf5ceca6b851a1393803b5823a0e2cf', phase='log_emit', boundary={'source': 'log', 'sink': 'log'}, candidate_policies=[{'policy_id': 'AI_AGENT_ACTIVITY_LOG', 'policy_name': 'Emit Agent Activity via OpenTelemetry', 'guardrail_id': None, 'policy_version': None}], fail_mode='ALLOW_WITH_AUDIT', source_type='agent', destination_type='log', project='lineaje-openclaw', organization='Enterprise', project_name='ai-chatbot', project_version='main', project_branch='main', components={'source': {'entity_type': 'agent', 'unique_org_id': 'vdna_1bOIDPqj97q6mzc6', 'repository_uri': 'https://github.com/abhijnya002/ai-chatbot', 'file_path': 'chatbot.py', 'line': 31, 'name': 'chatbot'}, 'identity': {'source': {'entity_type': 'aiagent', 'name': 'chatbot', 'version': '1.0.0', 'purl': 'pkg:aiagent/chatbot@1.0.0'}, 'app': {'name': 'ai-chatbot', 'version': 'main', 'purl': 'pkg:github/abhijnya002/ai-chatbot@main?commit-id=7cda29133ef56e84a0eede9c324ae7604c776dfe&commit-time=&build_file=requirements.txt&repo_strategy=single-repo'}}, 'invocation': {'file': 'chatbot.py', 'line': 37, 'function': ''}})
        try:
            reply = _gr_client.enforce(_gr_site, reply, content_type='application/json')
        except _gr_client.GuardrailUnavailableError:
            pass
        except PermissionError:
            pass
        print("AI:", reply)

        messages.append({"role": "assistant", "content": reply})

    except Exception as e:
        # LINEAJE: enforce() `e` at agent->log log_emit — scan flagged AI_DAT_SEC_012 (Mask PII on user interfaces). Mask/block; do not remove without review. site_id='site:sha256:6eb6961c74d7529817bbf771bbc7baa50e4a4bdc10f3095a6ad3a6d0ca1f8da3'
        _gr_client = _lineaje_load_gr_client()
        _gr_site = _gr_client.SiteDescriptor(site_id='site:sha256:6eb6961c74d7529817bbf771bbc7baa50e4a4bdc10f3095a6ad3a6d0ca1f8da3', phase='log_emit', boundary={'source': 'log', 'sink': 'log'}, candidate_policies=[{'policy_id': 'AI_AGENT_ACTIVITY_LOG', 'policy_name': 'Emit Agent Activity via OpenTelemetry', 'guardrail_id': None, 'policy_version': None}], fail_mode='ALLOW_WITH_AUDIT', source_type='agent', destination_type='log', project='lineaje-openclaw', organization='Enterprise', project_name='ai-chatbot', project_version='main', project_branch='main', components={'source': {'entity_type': 'agent', 'unique_org_id': 'vdna_1bOIDPqj97q6mzc6', 'repository_uri': 'https://github.com/abhijnya002/ai-chatbot', 'file_path': 'chatbot.py', 'line': 31, 'name': 'chatbot'}, 'identity': {'source': {'entity_type': 'aiagent', 'name': 'chatbot', 'version': '1.0.0', 'purl': 'pkg:aiagent/chatbot@1.0.0'}, 'app': {'name': 'ai-chatbot', 'version': 'main', 'purl': 'pkg:github/abhijnya002/ai-chatbot@main?commit-id=7cda29133ef56e84a0eede9c324ae7604c776dfe&commit-time=&build_file=requirements.txt&repo_strategy=single-repo'}}, 'invocation': {'file': 'chatbot.py', 'line': 42, 'function': ''}})
        try:
            e = _gr_client.enforce(_gr_site, e, content_type='application/json')
        except _gr_client.GuardrailUnavailableError:
            pass
        except PermissionError:
            pass
        print("Error:", e)