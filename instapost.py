class Instapost:
  def __init__(self):
    self.id = ''
    self.shortcode = ''
    #self.dimensions = {}
    #self.dimensions['width'] = 0
    #self.dimensions['height'] = 0
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
    #self.owner = '' self.userid = ''
    self.userid = ''
    self.username = ''
    self.is_video = False
    self.has_upcoming_event = False
    self.accessibility_caption = ''
    self.tagged_user_list = []
    self.caption = ''
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
