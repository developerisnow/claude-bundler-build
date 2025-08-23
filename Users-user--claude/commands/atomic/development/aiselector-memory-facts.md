# 🧠 MEMORY FACTS (Critical Production Knowledge)
<memory_facts>
  <api_integrations>
    <!-- IQData API -->
    - IQData API works with IP 34.86.160.219 (whitelisted)
    - IQData integration requires exact IP match for authentication
    - Always verify IP whitelist before troubleshooting API failures
    
    <!-- Discord API -->
    - Discord is BLOCKED in Turkey (court order)
    - Always check geographic restrictions before debugging timeouts
    - VPN required for Discord tools in Turkey
    - DiscordChatExporter needs manual installation (not in brew)
    
    <!-- OpenAI API -->
    - OpenAI active runs require wait logic up to 60 seconds
    - OpenAI API calls must include proper timeout handling
    - Active runs status polling prevents hung processes
  </api_integrations>
  
  <infrastructure>
    <!-- Cloud Jobs -->
    - Cloud Jobs use VPC connector bds-connector + Cloud NAT
    - VPC connector enables private network communication
    - Cloud NAT provides stable outbound IP (34.86.160.219)
    
    <!-- Redis -->
    - Redis can be completely disabled - system works without it
    - Redis is used for caching only, not critical data
    - Make Redis optional in all new services
    
    <!-- NATS -->
    - NATS library v2.8.0 is more stable than v2.10.0
    - Use v2.8.0 for production deployments
    - Version conflicts cause connection issues
  </infrastructure>
  
  <data_validation>
    <!-- Selection Processing -->
    - Selection requires mandatory fields: audience_language_id, user_language_id
    - NULL checks must be performed before Cloud Jobs processing
    - Foreign key constraints must be verified before UPDATE operations
    
    <!-- Database -->
    - Always check foreign key constraints before UPDATE statements
    - NULL field validation prevents downstream job failures
    - Database validation catches errors early in pipeline
  </data_validation>
  
  <common_mistakes>
    <!-- Database -->
    - ❌ Not checking foreign key constraints before UPDATE
    - ❌ Forgetting NULL field validation in Cloud Jobs
    - ❌ Not verifying selection requirements before processing
    
    <!-- External APIs -->
    - ❌ Forgetting IP whitelisting for external APIs
    - ❌ Not implementing Redis graceful fallback
    - ❌ Missing timeout handling for OpenAI active runs
    
    <!-- Infrastructure -->
    - ❌ Not checking secret versions in Cloud Run
    - ❌ Using unstable NATS library versions
    - ❌ Not making Redis optional in new services
  </common_mistakes>
  
  <operational_rules>
    <!-- Log Analysis -->
    - Always use sub-agents for log analysis > 50 lines
    - Use parallel processing for multiple service logs
    - Preserve main context for reasoning, not data parsing
    
    <!-- Testing -->
    - Check git status before cloud testing
    - Always verify IP whitelisting before API testing
    - Create smoke tests for external API integrations
    
    <!-- Deployment -->
    - Make Redis optional in all new services
    - Use NATS v2.8.0 for stability
    - Always verify VPC connector configuration
  </operational_rules>
</memory_facts>