import json

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
    print(self.timestamp)
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
