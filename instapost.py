import json

class Instauser:
  def __init__(self):
    self.ai_agent_type = ''
    self.biography = ''
    self.bio_links = []
    self.fb_profile_biolink = ''
    self.blocked_by_viewer = False
    self.restricted_by_viewer = False
    self.country_block = False
    self.eimu_id = ''
    self.external_url = ''
    self.external_url_linkshimmed = ''
    self.followed_by_count = 0
    self.fbid = 0
    self.followed_by_viewer = False
    self.follow_count = 0
    self.follows_viewer = False
    self.full_name = False
    self.group_metadata = ''
    self.has_ar_effects = False
    self.has_clips = False
    self.has_guides = False
    self.has_channel = False
    self.has_blocked_viewer = False
    self.highlight_reel_count = 0
    self.has_requested_viewer = False
    self.hide_like_and_view_count = False
    self.id = ''
    self.is_business_account = False
    self.is_professional_account = False
    self.is_supervision_enabled = False
    self.is_guardian_of_viewer = False
    self.is_supervised_by_viewer = False
    self.is_supervised_user = False
    self.is_embeds_disabled = False
    self.is_joined_recently = False
    self.guardian_id = ''
    self.business_address_json = ''
    self.business_contact_method = ''
    self.business_phone_number = ''
    self.business_category_name = ''
    self.overall_category_name = ''
    self.category_enum = ''
    self.category_name = ''
    self.is_private = False
    self.is_verified = False
    self.is_verified_by_mv4b = False
    self.is_regulated_c18 = False
    self.mutual_followed_by_count = 0
    self.mutual_followed_by_list = []
    self.pinned_channels_list_count = 0
    self.profile_pic_url = ''
    self.profile_pic_url_hd = ''
    self.requested_by_viewer = False
    self.should_show_category = False
    self.should_show_public_contacts = False
    self.show_account_transparency_details = False
    self.transparency_label = ''
    self.transparency_product = ''
    self.username = ''
    self.connected_fb_page = ''
    self.pronouns = []

  def dumph(self):
    thishash['ai_agent_type'] = self.ai_agent_type
    thishash['biography'] = self.biography
    thishash['bio_links'] = self.bio_links
    thishash['fb_profile_biolink'] = self.fb_profile_biolink
    thishash['blocked_by_viewer'] = self.blocked_by_viewer
    thishash['restricted_by_viewer'] = self.restricted_by_viewer
    thishash['country_block'] = self.country_block
    thishash['eimu_id'] = self.eimu_id
    thishash['external_url'] = self.external_url
    thishash['external_url_linkshimmed'] = self.external_url_linkshimmed
    thishash['followed_by_count'] = self.followed_by_count
    thishash['fbid'] = self.fbid
    thishash['followed_by_viewer'] = self.followed_by_viewer
    thishash['follow_count'] = self.follow_count
    thishash['follows_viewer'] = self.follows_viewer
    thishash['full_name'] = self.full_name
    thishash['group_metadata'] = self.group_metadata
    thishash['has_ar_effects'] = self.has_ar_effects
    thishash['has_clips'] = self.has_clips
    thishash['has_guides'] = self.has_guides
    thishash['has_channel'] = self.has_channel
    thishash['has_blocked_viewer'] = self.has_blocked_viewer
    thishash['highlight_reel_count'] = self.highlight_reel_count
    thishash['has_requested_viewer'] = self.has_requested_viewer
    thishash['hide_like_and_view_count'] = self.hide_like_and_view_count
    thishash['id'] = self.id
    thishash['is_business_account'] = self.is_business_account
    thishash['is_professional_account'] = self.is_professional_account
    thishash['is_supervision_enabled'] = self.is_supervision_enabled
    thishash['is_guardian_of_viewer'] = self.is_guardian_of_viewer
    thishash['is_supervised_by_viewer'] = self.is_supervised_by_viewer
    thishash['is_supervised_user'] = self.is_supervised_user
    thishash['is_embeds_disabled'] = self.is_embeds_disabled
    thishash['is_joined_recently'] = self.is_joined_recently
    thishash['guardian_id'] = self.guardian_id
    thishash['business_address_json'] = self.business_address_json
    thishash['business_contact_method'] = self.business_contact_method
    thishash['business_phone_number'] = self.business_phone_number
    thishash['business_category_name'] = self.business_category_name
    thishash['overall_category_name'] = self.overall_category_name
    thishash['category_enum'] = self.category_enum
    thishash['category_name'] = self.category_name
    thishash['is_private'] = self.is_private
    thishash['is_verified'] = self.is_verified
    thishash['is_verified_by_mv4b'] = self.is_verified_by_mv4b
    thishash['is_regulated_c18'] = self.is_regulated_c18
    thishash['mutual_followed_by_count'] = self.mutual_followed_by_count
    thishash['mutual_followed_by_list'] = self.mutual_followed_by_list
    thishash['pinned_channels_list_count'] = self.pinned_channels_list_count
    thishash['profile_pic_url'] = self.profile_pic_url
    thishash['profile_pic_url_hd'] = self.profile_pic_url_hd
    thishash['requested_by_viewer'] = self.requested_by_viewer
    thishash['should_show_category'] = self.should_show_category
    thishash['should_show_public_contacts'] = self.should_show_public_contacts
    thishash['show_account_transparency_details'] = self.show_account_transparency_details
    thishash['transparency_label'] = self.transparency_label
    thishash['transparency_product'] = self.transparency_product
    thishash['username'] = self.username
    thishash['connected_fb_page'] = self.connected_fb_page
    thishash['pronouns'] = self.pronouns
    return thishash

  def dumps(self):
    thishash = self.dumph()
    return json.dumps(thishash)

  def reads(self,json):
    thishash = json.reads(json)
    postobject = self.Instauser()
    return postobject

  def readh(self,thishash):
    self.ai_agent_type = thishash['ai_agent_type']
    self.biography = thishash['biography']
    self.bio_links = thishash['bio_links']
    self.fb_profile_biolink = thishash['fb_profile_biolink']
    self.blocked_by_viewer = thishash['blocked_by_viewer']
    self.restricted_by_viewer = thishash['restricted_by_viewer']
    self.country_block = thishash['country_block']
    self.eimu_id = thishash['eimu_id']
    self.external_url = thishash['external_url']
    self.external_url_linkshimmed = thishash['external_url_linkshimmed']
    self.followed_by_count = thishash['followed_by_count']
    self.fbid = thishash['fbid']
    self.followed_by_viewer = thishash['followed_by_viewer']
    self.follow_count = thishash['follow_count']
    self.follows_viewer = thishash['follows_viewer']
    self.full_name = thishash['full_name']
    self.group_metadata = thishash['group_metadata']
    self.has_ar_effects = thishash['has_ar_effects']
    self.has_clips = thishash['has_clips']
    self.has_guides = thishash['has_guides']
    self.has_channel = thishash['has_channel']
    self.has_blocked_viewer = thishash['has_blocked_viewer']
    self.highlight_reel_count = thishash['highlight_reel_count']
    self.has_requested_viewer = thishash['has_requested_viewer']
    self.hide_like_and_view_count = thishash['hide_like_and_view_count']
    self.id = thishash['id']
    self.is_business_account = thishash['is_business_account']
    self.is_professional_account = thishash['is_professional_account']
    self.is_supervision_enabled = thishash['is_supervision_enabled']
    self.is_guardian_of_viewer = thishash['is_guardian_of_viewer']
    self.is_supervised_by_viewer = thishash['is_supervised_by_viewer']
    self.is_supervised_user = thishash['is_supervised_user']
    self.is_embed_disabled = thishash['is_embeds_disabled']
    self.is_joined_recently = thishash['is_joined_recently']
    self.guardian_id = thishash['guardian_id']
    self.business_address_json = thishash['business_address_json']
    self.business_contact_method = thishash['business_contact_method']
    self.business_phone_number = thishash['business_phone_number']
    self.business_category_name = thishash['business_category_name']
    self.overall_category_name = thishash['overall_category_name']
    self.category_enum = thishash['category_enum']
    self.category_name = thishash['category_name']
    self.is_private = thishash['is_private']
    self.is_verified = thishash['is_verified']
    self.is_verified_by_mv4b = thishash['is_verified_by_mv4b']
    self.is_regulated_c18 = thishash['is_regulated_c18']
    self.mutual_followed_by_count = thishash['mutual_followed_by_count']
    self.mutual_followed_by_list = thishash['mutual_followed_by_list']
    self.pinned_channels_list_count = thishash['pinned_channels_list_count']
    self.profile_pic_url = thishash['profile_pic_url']
    self.profile_pic_url_hd = thishash['profile_pic_url_hd']
    self.requested_by_viewer = thishash['requested_by_viewer']
    self.should_show_category = thishash['should_show_category']
    self.should_show_public_contacts = thishash['should_show_public_contacts']
    self.show_account_transparency_details = thishash['show_account_transparency_details']
    self.transparency_label = thishash['transparency_label']
    self.transparency_product = thishash['transparency_product']
    self.username = thishash['username']
    self.connected_fb_page = thishash['connected_fb_page']
    self.pronouns = thishash['pronouns']

class Instapost:
  def __init__(self):
    self.id = ''
    self.shortcode = ''
    self.width = 0
    self.height = 0
    self.display_url = ''
    self.tagged_user_list = []
    self.fact_check_overall_rating = ''
    self.fact_check_information = ''
    self.gating_info = ''
    self.sharing_friction_info = ''
    self.media_overlay_info = ''
    self.media_preview = ''
    self.userid = ''
    self.username = ''
    self.is_video = False
    self.has_upcoming_event = False
    self.accessibility_caption = ''
    self.tagged_user_list = []
    self.caption = ''
##############################################################################
    self.number_of_comments = ''
    self.comments_disabled = False
    self.timestamp = 0
    self.number_of_likes = ''
##############################################################################
    self.location = ''
    self.sidecar_to_children_list = []

  def get_common_values(self,thisnode):
    self.id = thisnode.get('id','')
    self.shortcode = thisnode.get('shortcode','')
    #subfields
    height = ''
    width = ''
    dimensions = thisnode.get('dimensions',{})
    if dimensions:
      width = dimensions.get('width','')
      height = dimensions.get('height','')
    self.width = width
    self.height = height
    self.display_url = thisnode.get('display_url','')
    self.tagged_user_list = thisnode.get('edge_media_to_tagged_user',[])
    self.fact_check_overall_rating = thisnode.get('fact_check_overall_rating','')
    self.fact_check_information = thisnode.get('fact_check_information','')
    self.gating_info = thisnode.get('gating_info','')
    self.sharing_friction_info = thisnode.get('sharing_friction_info','')
    self.media_overlay_info = thisnode.get('media_overlay_info','')
    self.media_preview = thisnode.get('media_preview','')
    # subfields
    userid = ''
    username = ''
    owner = thisnode.get('owner',{})
    if owner:
      userid = owner.get('id','')
      username = owner.get('username','')
    self.userid = userid
    self.username = username
    self.is_video = thisnode.get('is_video',False)
    self.has_upcoming_event = thisnode.get('has_upcoming_event',False)
    self.accessibility_caption = thisnode.get('accessibility_caption','')

  def process_post(self,thisnode):
    self.get_common_values(thisnode)
    # after this point everything is attached only to the main post
    caption = ''
    if thisnode.get('edge_media_to_caption',''):
      captionlist = thisnode['edge_media_to_caption']['edges']
      if captionlist:
        caption = captionlist[0]
    self.caption = caption
##############################################################################
    number_of_comments = 0
    if thisnode.get('edge_media_to_comment',{}):
      if thisnode['edge_media_to_comment'].get('count',0):
        number_of_comments = thisnode['edge_media_to_comment']['count']
    self.number_of_comments = number_of_comments
    self.comments_disabled = thisnode.get('comments_disabled', False)
    self.timestamp = thisnode.get('taken_at_timestamp',0)
    number_of_likes = ''
    if thisnode.get('edge_media_preview_like',{}):
      if thisnode['edge_media_preview_like'].get('count',0):
        number_of_likes = thisnode['edge_media_preview_like']['count']
    self.number_of_likes = number_of_likes
##############################################################################
    self.location = thisnode.get('location','')
    # after this point these values only exist if we have subposts 
    my_sidecar_to_children_list = []
    sidecar_to_children = thisnode.get('edge_sidecar_to_children',{})
    if sidecar_to_children:
      sidecar_to_children_list = sidecar_to_children.get('edges',[])
      if sidecar_to_children_list:
        for childthing in sidecar_to_children_list:
          thissubnode = childthing.get('node',{})
          if thissubnode:
            # create new post object
            mysubpost = Instapost()
            # grab the stuff only attached to main
            mysubpost.caption = self.caption
            mysubpost.location = self.location
            mysubpost.get_common_values(thissubnode)
            my_sidecar_to_children_list.append(mysubpost)
    self.sidecar_to_children_list = my_sidecar_to_children_list

  # this really does not belong under posts but okay for now until we get maybe broader
  def get_app_id(username):
    debug = False
    request_url = 'https://www.instagram.com/' + username + '/'
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/118.0'}
    if not debug:
      proxies = {}
    else:
      proxies = {
        'http' : 'http://localhost:8888',
        'https' : 'http://localhost:8888',
      }
    response = requests.get(request_url, headers=headers, proxies=proxies, verify=False)
    raw_html = response.text
    responselines = response.text.splitlines()
    for thisline in responselines:
      hit = re.search(r"APP_ID",thisline)
      if hit:
        jsonthisline = re.findall(r"<script[^>]*>\s*(.*?)\s*</script>",thisline)
        if jsonthisline:
          jsontext = jsonthisline[0]
          # this json is so disorganized it's not even worth parsing
          #thishash = json.loads(jsontext)
          app_id_hits = re.findall(r"\"APP_ID\":\"(.*?)\"",jsontext)
          app_id = app_id_hits[0]
          return app_id

  def dumph(self):
    posthash = {}
    posthash['id'] = self.id
    posthash['shortcode'] = self.shortcode
    posthash['width'] = self.width
    posthash['height'] = self.height
    posthash['display_url'] = self.display_url
    posthash['tagged_user_list'] = self.tagged_user_list
    posthash['fact_check_overall_rating'] = self.fact_check_overall_rating
    posthash['fact_check_information'] = self.fact_check_information
    posthash['gating_info'] = self.gating_info
    posthash['sharing_friction_info'] = self.sharing_friction_info
    posthash['media_overlay_info'] = self.media_overlay_info
    posthash['media_preview'] = self.media_preview
    posthash['userid'] = self.userid
    posthash['username'] = self.username
    posthash['is_video'] = self.is_video
    posthash['has_upcoming_event'] = self.has_upcoming_event
    posthash['accessibility_caption'] = self.accessibility_caption
    posthash['tagged_user_list'] = self.tagged_user_list
    posthash['caption'] = self.caption
##############################################################################
    posthash['number_of_comments'] = self.number_of_comments
    posthash['comments_disabled'] = self.comments_disabled
    posthash['timestamp'] = self.timestamp
    posthash['number_of_likes'] = self.number_of_likes
##############################################################################
    posthash['location'] = self.location
    sidecar_to_children_list_data = []
    for this_child in self.sidecar_to_children_list:
      thishash = this_child.dumph()
      sidecar_to_children_list_data.append(thishash)
    posthash['sidecar_to_children_list'] = sidecar_to_children_list_data
    return posthash

  def dumps(self):
    thishash = self.dumph()
    return json.dumps(thishash)

  def reads(self,json):
    thishash = json.reads(json)
    postobject = self.Instapost()
    return postobject

  def readh(self,posthash):
    self.id = posthash['id']
    self.shortcode = posthash['shortcode']
    self.width = posthash['width']
    self.height = posthash['height']
    self.display_url = posthash['display_url']
    self.tagged_user_list = posthash['tagged_user_list']
    self.fact_check_overall_rating = posthash['fact_check_overall_rating']
    self.fact_check_information = posthash['fact_check_information']
    self.gating_info = posthash['gating_info']
    self.sharing_friction_info =  posthash['sharing_friction_info']
    self.media_overlay_info = posthash['media_overlay_info']
    self.media_preview = posthash['media_preview']
    self.userid = posthash['userid']
    self.username = posthash['username']
    self.is_video = posthash['is_video']
    self.has_upcoming_event = posthash['has_upcoming_event']
    self.accessibility_caption = posthash['accessibility_caption']
    self.tagged_user_list = posthash['tagged_user_list']
    self.caption = posthash['caption']
##############################################################################
    self.number_of_comments = posthash['number_of_comments']
    self.comments_disabled = posthash['comments_disabled']
    self.timestamp = posthash['timestamp']
    self.number_of_likes = posthash['number_of_likes']
##############################################################################
    self.location = posthash['location']
    sidecar_to_children_list_posts = []
    for this_child in posthash['sidecar_to_children_list']:
      thispost = this_child.readh()
      sidecar_to_children_list_posts.append(thispost)
    self.sidecar_to_children_list = posthash['sidecar_to_children_list']

