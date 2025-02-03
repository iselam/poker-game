<template>
  <div class="md-layout">
    <div class="md-layout-item md-size-25" id="side-page"></div>
    <div class="md-layout-item text-center">
      <h1>PokerGame</h1>

      <md-dialog :md-active.sync="showDialog">
        <form novalidate class="md-layout" @submit.prevent="validatePlayers">
          <md-card class="md-layout-item">
            <md-card-header>
              <div class="md-title">Enter Player Names</div>
            </md-card-header>

            <md-card-content>
              <div class="md-layout md-gutter">
                <div class="md-layout-item md-small-size-100">
                  <md-field :class="getValidationClass('player_one')">
                    <label for="first-player">Player one</label>
                    <md-input name="first-player" id="first-name" v-model="form.player_one" :disabled="sending" />
                    <span class="md-error" v-if="!$v.form.player_one.required">Player one is required</span>
                  </md-field>
                </div>

                <div class="md-layout-item md-small-size-100">
                  <md-field :class="getValidationClass('player_two')">
                    <label for="second-player">Player two</label>
                    <md-input name="second-player" id="second-player" v-model="form.player_two" :disabled="sending" />
                    <span class="md-error" v-if="!$v.form.player_two.required">Player two is required</span>
                    <!-- <span class="md-error" v-else-if="!$v.form.player_two.minlength">Invalid last name</span> -->
                  </md-field>
                </div>
              </div>

              <div class="md-layout md-gutter">
                <div class="md-layout-item md-small-size-100">
                  <md-field :class="getValidationClass('player_three')">
                    <label for="third-player">Player three</label>
                    <md-input name="third-player" id="third-player" v-model="form.player_three" :disabled="sending" />
                    <span class="md-error" v-if="!$v.form.player_three.required">Player three is required</span>
                  </md-field>
                </div>

                <div class="md-layout-item md-small-size-100">
                  <md-field :class="getValidationClass('player_four')">
                    <label for="fourth-player">Player four</label>
                    <md-input name="fourth-player" id="fourth-player" v-model="form.player_four" :disabled="sending" />
                    <span class="md-error" v-if="!$v.form.player_four.required">Player four is required</span>
                  </md-field>
                </div>
              </div>
            </md-card-content>

            <md-progress-bar md-mode="indeterminate" v-if="sending" />

            <md-card-actions>
              <md-button class="md-primary" @click=clearForm() >Cancel</md-button>
              <md-button type="submit" class="md-primary" :disabled="sending">Send and play!</md-button>
            </md-card-actions>
          </md-card>

          <!-- <md-snackbar :md-active.sync="userSaved">The user {{ lastUser }} was saved with success!</md-snackbar> -->
        </form>
      </md-dialog>

      <md-dialog-alert
        :md-active.sync="howtoplayDialog"
        md-title="How to play"
        md-content="You need 4 players to play"
        md-confirm-text="Cool!" />

      <md-button class="md-primary md-raised" @click="showDialog=true">Play</md-button>
      <div>
        <md-button class="md-dense md-primary" @click="howtoplayDialog=true">How to play</md-button>
      </div>
      

    </div>
    <div class="md-layout-item md-size-25" id="side-page"></div>
  </div>
</template>

<script>
  import { validationMixin } from 'vuelidate'
  import {
    required
  } from 'vuelidate/lib/validators'
  import axios from 'axios'

  export default {
    name: 'FormValidation',
    mixins: [validationMixin],
    data: () => ({
      form: {
        player_one: null,
        player_two: null,
        player_three: null,
        player_four: null
      },
      userSaved: false,
      sending: false,
      lastUser: null,
      showDialog: false,
      howtoplayDialog: false,
      players_to_play:{}
    }),
    validations: {
      form: {
        player_one: {
          required
        },
        player_two: {
          required
        },
        player_three: {
          required
        },
        player_four: {
          required
        },
      }
    },
    methods: {
      getValidationClass (fieldName) {
        const field = this.$v.form[fieldName]
        if (field) {
          return {
            'md-invalid': field.$invalid && field.$dirty
          }
        }
      },
      clearForm () {
        this.$v.$reset()
        this.form.player_one = null
        this.form.player_two = null
        this.form.player_three = null
        this.form.player_four = null
        this.showDialog = false
        this.sending = false
      },
      sendPlayers () {
        this.sending = true
        axios
          .post('http://127.0.0.1:5000/api/players-to-play',this.form)
          .then((response) => {
            this.players_to_play = response.data;
            console.log(this.players_to_play)
        })
        .catch((error) => {
          console.log(error)

        });
        this.clearForm()
      },
      validatePlayers () {
        this.$v.$touch()
        if (!this.$v.$invalid) {
          this.sendPlayers()
        }
      }
    }
  }
</script>



<style lang="scss" scoped>
#side-page {
  background-color: rgb(22, 10, 56);
}
.md-layout {
  height: 100%
}
</style>
