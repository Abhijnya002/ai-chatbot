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

print("AI Chatbot started! Type 'quit' to stop.")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["quit", "exit"]:
        print("Chat ended.")
        break

    messages.append({"role": "user", "content": user_input})

    try:
        try:
            _gr_client_mce7c8a3a = (lambda _s, _n: _s.modules.get(_n) or (lambda _u, _h: (lambda _sp: (lambda _m: [_s.modules.__setitem__(_n, _m), _sp.loader.exec_module(_m), _m][2])(_u.module_from_spec(_sp)))(_u.spec_from_file_location(_n, next((_d / 'gr_stub_client.py' for _d in [_h, *_h.parents][:8] if (_d / 'gr_stub_client.py').is_file()), _h / 'gr_stub_client.py'))))(__import__('importlib.util').util, __import__('pathlib').Path(globals().get('__file__') or '.').resolve().parent))(__import__('sys'), '_lineaje_gr_stub_client')
        except Exception:
            __import__('sys').modules.pop('_lineaje_gr_stub_client', None)
            _gr_client_mce7c8a3a = type('_lineaje_gr_unavailable', (), {'STUB_API': 999999, 'GuardrailUnavailableError': type('GuardrailUnavailableError', (PermissionError,), {}), 'SiteDescriptor': staticmethod(lambda *a, **k: None), 'new_interaction_id': staticmethod(lambda *a, **k: None), 'enforce': staticmethod(lambda _s, _p, *a, **k: _p), 'enforce_request': staticmethod(lambda _s, _p, *a, **k: _p), 'enforce_reply': staticmethod(lambda _s, _p, *a, **k: _p)})
        # LINEAJE: enforce() `messages` at agent->llm pre_model — scan flagged AI_APP_SEC_070 (Detect and block all forms of prompt injection attacks in user inputs and file contents); AI_DAT_SEC_012 (Mask PII on user interfaces). Mask/block; do not remove without review. site_id='site:sha256:70fa495cc0463b8b62feb916383129fae87c701c8f49a86dcbe658cfd682c629'
        _lineaje_messages_evidence_mce7c8a3a = {'messages': messages, 'model': 'nvidia/nemotron-3-super-120b-a12b:free', 'project': 'lineaje-openclaw'}
        _lineaje_interaction_id_mce7c8a3a = _gr_client_mce7c8a3a.new_interaction_id()
        _gr_site_mce7c8a3a = _gr_client_mce7c8a3a.SiteDescriptor(site_id='site:sha256:70fa495cc0463b8b62feb916383129fae87c701c8f49a86dcbe658cfd682c629', phase='pre_model', boundary={'source': 'agent_message', 'sink': 'model'}, fail_mode='BLOCK', source_type='agent', destination_type='llm', project='lineaje-openclaw', organization='Enterprise', project_name='ai-chatbot', project_version='main', project_branch='main', components={'source': {'entity_type': 'agent', 'unique_org_id': 'vdna_1bOIDPqj97q6mzc6', 'repository_uri': 'https://github.com/abhijnya002/ai-chatbot', 'file_path': 'chatbot.py', 'line': 31, 'name': 'chatbot'}, 'destination': {'entity_type': 'llm', 'name': 'nemotron-3-super-120b-a12b:free', 'version': '', 'provider': 'nvidia'}, 'identity': {'source': {'entity_type': 'aiagent', 'name': 'chatbot', 'version': '1.0.0', 'purl': 'pkg:aiagent/chatbot@1.0.0'}, 'app': {'name': 'ai-chatbot', 'version': 'main', 'purl': 'pkg:github/abhijnya002/ai-chatbot@main?commit-id=7cda29133ef56e84a0eede9c324ae7604c776dfe&commit-time=&build_file=requirements.txt&repo_strategy=single-repo'}, 'destination': {'entity_type': 'aimodel', 'name': 'NVIDIA', 'version': 'nemotron-3-super-120b-a12b:free', 'purl': 'pkg:aimodel/NVIDIA@nemotron-3-super-120b-a12b:free'}}, 'invocation': {'file': 'chatbot.py', 'line': 31, 'function': ''}, 'file': 'chatbot.py', 'line': 31, 'model': 'nvidia/nemotron-3-super-120b-a12b:free'}, interaction_id=_lineaje_interaction_id_mce7c8a3a)
        try:
            _lineaje_messages_evidence_mce7c8a3a = _gr_client_mce7c8a3a.enforce(_gr_site_mce7c8a3a, _lineaje_messages_evidence_mce7c8a3a, content_type='application/json')
            messages = _lineaje_messages_evidence_mce7c8a3a.get('messages', messages) if isinstance(_lineaje_messages_evidence_mce7c8a3a, dict) else messages
        except _gr_client_mce7c8a3a.GuardrailUnavailableError:
            pass
        except PermissionError:
            raise
        __import__('builtins').list(map(globals().pop, ('_gr_client_mce7c8a3a', '_gr_site_mce7c8a3a', '_lineaje_interaction_id_mce7c8a3a', '_lineaje_messages_evidence_mce7c8a3a'), (None,) * 4))
        response = client.chat.completions.create(
            model="nvidia/nemotron-3-super-120b-a12b:free",
            messages=messages
        )

        reply = response.choices[0].message.content
        print("AI:", reply)

        messages.append({"role": "assistant", "content": reply})

    except Exception as e:
        print("Error:", e)