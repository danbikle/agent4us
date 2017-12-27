require 'test_helper'

class CclassesControllerTest < ActionDispatch::IntegrationTest
  test "should get index" do
    get cclasses_index_url
    assert_response :success
  end

end
